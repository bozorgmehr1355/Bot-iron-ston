
# bot.py - Telegram Price Bot (Clean & Optimized Version)

import os
import json
import time
import threading
import requests
import re
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application, 
    CommandHandler, 
    CallbackQueryHandler, 
    MessageHandler, 
    filters, 
    ConversationHandler,
    ContextTypes
)
from datetime import datetime
from bs4 import BeautifulSoup

# ═══════════════════════════════════════════════════════════════════
# 1) CONFIGURATION
# 

═══════════════════════════════════════════════════════════════════

TOKEN = os.environ.get("BOT_TOKEN")
METALPRICE_API_KEY = os.environ.get("METALPRICE_API_KEY")
ADMIN_ID = 715854466
SCRAPER_SECRET = os.environ.get("SCRAPER_SECRET", "change_this_secret")

# File paths
RATE_FILE = "rates.json"
PRICE_FILE = "prices.json"
WORLD_PRICE_FILE = "world_prices.json"
METALS_FILE = "metals_prices.json"
FACTORY_PRICE_FILE = "factory_prices.json"

# Conversation states
WAITING_VALUE = 1

# Thread-safe file access
_file_lock = threading.Lock()

# Default factory data structure
DEFAULT_FACTORY_DATA = {
    "rebar": {
        "اصفهان": {"ذوبآهن": 58000, "فولاد مبارکه": 57500},
        "خوزستان": {"فولاد خوزستان": 58200}

    },
    "billet": {
        "اصفهان": {"ذوبآهن": 42500, "فولاد مبارکه": 42000},
        "خوزستان": {"فولاد خوزستان": 42800}
    },
    "dri": {
        "خراسان": {"فولاد خراسان": 14166}
    },
    "pellet": {
        "خراسان": {"گلگهر": 6500000}
    },
    "concentrate": {
        "کرمان": {"گلگهر": 4800000}
    }
}

# ═══════════════════════════════════════════════════════════════════
# 2) HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

def to_persian(num):
    """Convert English digits to Persian"""
    persian_digits = "۰۱۲۳۴۵۶۷۸۹"
    return "".join(persian_digits[int(d)] if d.isdigit() else d for d in str(num))


def format_number(num):
    """Format number with commas and Persian digits"""
    try:
        formatted = f"{int(num):,}"
        return to_persian(formatted)
    except:
        return to_persian(str(num))

def format_float(num, decimals=2):
    """Format float with Persian digits"""
    try:
        formatted = f"{float(num):.{decimals}f}"
        return to_persian(formatted)
    except:
        return to_persian(str(num))

def save_json(filepath, data):
    """Thread-safe JSON save"""
    with _file_lock:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

def load_json(filepath, default):
    """Thread-safe JSON load with fallback"""
    with _file_lock:
        if not os.path.exists(filepath):
            return default
        try:

            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return default

def is_admin(update: Update) -> bool:
    """Check if user is admin"""
    return update.effective_user.id == ADMIN_ID

# ═══════════════════════════════════════════════════════════════════
# 3) DATA UPDATE FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

def update_rates():
    """Update exchange rates from Nobitex API"""
    try:
        response = requests.get(
            "https://api.nobitex.ir/v2/orderbook/USDTIRT",
            timeout=10
        )
        data = response.json()
        free_rate = int(float(data["asks"][0][0]))
        
        rates = {
            "free": free_rate,

            "secondary": 140000,  # Default secondary rate
            "last_update": datetime.now().isoformat()
        }
        save_json(RATE_FILE, rates)
        print(f"✓ Rates updated: {free_rate}")
    except Exception as e:
        print(f"✗ Rate update failed: {e}")
        # Save fallback
        save_json(RATE_FILE, {
