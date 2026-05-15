
# config.py
import os

# ═══════════════════════════════════════════════════════════
# تنظیمات اصلی ربات
# ═══════════════════════════════════════════════════════════

# توکن ربات تلگرام (از @BotFather دریافت کنید)
TOKEN = "8718722839:AAG9tP8gB_4sOwVOCA_nUR8P17C1TrIqOjA"

# شناسه عددی ادمین (از @userinfobot دریافت کنید)
ADMIN_ID = 715854466

# کلید API برای قیمتهای جهانی فلزات
METALPRICE_API_KEY = "e6de2613ce5902f03d502dff62d5f83c"

# کلید امنیتی برای اسکریپر (برای API داخلی)
SCRAPER_SECRET = "bceeeed5a31738e16428971130b92694"

# ═══════════════════════════════════════════════════════════
# مسیرهای فایلهای داده
# 

═══════════════════════════════════════════════════════════

DATA_DIR = "data"
RATES_FILE = os.path.join(DATA_DIR, "rates.json")
PRICES_FILE = os.path.join(DATA_DIR, "prices.json")
WORLD_PRICES_FILE = os.path.join(DATA_DIR, "world_prices.json")
METALS_FILE = os.path.join(DATA_DIR, "metals.json")
FACTORY_PRICES_FILE = os.path.join(DATA_DIR, "factory_prices.json")

# ═══════════════════════════════════════════════════════════
# تنظیمات بهروزرسانی خودکار (ثانیه)
# ═══════════════════════════════════════════════════════════

UPDATE_INTERVAL_RATES = 300        # هر 5 دقیقه
UPDATE_INTERVAL_PRICES = 600       # هر 10 دقیقه
UPDATE_INTERVAL_WORLD = 3600       # هر 1 ساعت
UPDATE_INTERVAL_METALS = 3600      # هر 1 ساعت

# ═══════════════════════════════════════════════════════════
# URLهای منابع داده

# ═══════════════════════════════════════════════════════════

NOBITEX_API_URL = "https://api.nobitex.ir/v2/orderbook/USDTIRT"
AHANMELAL_BILLET_URL = "https://www.ahanmelal.com/price/billet"
AHANMELAL_REBAR_URL = "https://www.ahanmelal.com/price/rebar"
METALPRICE_API_URL = "https://api.metalpriceapi.com/v1/latest"

# ═══════════════════════════════════════════════════════════
# تنظیمات موتور جستجو
# ═══════════════════════════════════════════════════════════

SEARCH_MIN_QUERY_LENGTH = 2        # حداقل طول کلمه جستجو
SEARCH_MAX_RESULTS = 10            # حداکثر نتایج نمایش داده شده
