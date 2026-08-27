# 🛡️ سپر پارسی | PersianShield

![GitHub Actions](https://img.shields.io/badge/Auto--Update-Daily-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
![Platform](https://img.shields.io/badge/uBlock%20Origin-%E2%9C%93-orange?style=flat-square)
![Platform](https://img.shields.io/badge/AdGuard-%E2%9C%93-green?style=flat-square)
![Platform](https://img.shields.io/badge/Pi--hole-%E2%9C%93-red?style=flat-square)
![Platform](https://img.shields.io/badge/AdGuard%20Home-%E2%9C%93-purple?style=flat-square)

> **«یک لیست برای همیشه؛ خداحافظی با تبلیغات، ردیاب‌ها و بدافزارها!»**
>
> جامع‌ترین فیلتر لیست یکپارچه برای وب فارسی و جهانی. با اشتراک در این لیست، **نیاز شما به فعال‌سازی هر لیست دیگری برای همیشه از بین می‌رود.**

---

## 📖 فهرست مطالب

- [معرفی پروژه](#-معرفی-پروژه)
- [ویژگی‌های کلیدی](#-ویژگیهای-کلیدی)
- [لینک‌های اشتراک](#-لینکهای-اشتراک)
- [راهنمای نصب](#-راهنمای-نصب-و-فعالسازی)
- [منابع و لیست‌های استفاده شده](#-منابع-و-لیستهای-استفاده-شده)
- [ساختار فایل‌ها](#-ساختار-فایلها)
- [سوالات متداول](#-سوالات-متداول)
- [مشارکت](#-مشارکت)
- [توسعه‌دهنده](#-توسعهدهنده-و-ارتباط-با-ما)

---

## ✨ معرفی پروژه

وب فارسی پر از اسکریپت‌های تبلیغاتی خاص (مانند **یکتانت**، **مدیااد**، **صباویژن**، **کاپریلا** و **نجات‌نت**) و پاپ‌آپ‌های مزاحم (مثل دعوت به کانال‌های تلگرام) است که لیست‌های خارجی قادر به شناسایی آن‌ها نیستند. از سوی دیگر، لیست‌های فارسی موجود در اینترنت اغلب پوشش کاملی برای تبلیغات جهانی، ردیاب‌های مدرن و بدافزارها ندارند.

پروژه **PersianShield (سپر پارسی)** با استفاده از قدرت **GitHub Actions**، هر ۲۴ ساعت به‌صورت خودکار بهترین و قدرتمندترین فیلترهای جهان را با لیست‌های اختصاصی فارسی ترکیب می‌کند. این اسکریپت هوشمند:

- ✅ قوانین تکراری را حذف می‌کند
- ✅ فرمت‌های مختلف (hosts, adblock, domain) را به یک استاندارد واحد تبدیل می‌کند
- ✅ منابع را به‌صورت خودکار به‌روزرسانی می‌کند
- ✅ قوانین سفارشی شما (فایل `extra.txt`) را ادغام می‌کند

---

## 🌟 ویژگی‌های کلیدی

| ویژگی | توضیحات |
|:---|:---|
| 🚫 **مسدودسازی تبلیغات** | بنرها، ویدیوهای تبلیغاتی، پاپ‌آپ‌ها و اسکریپت‌های ضد-ادبلاک |
| 🕵️ **حفاظت از حریم خصوصی** | ردیاب‌ها، اسکریپت‌های جاسوسی و تحلیل‌های رفتاری |
| 🛡️ **امنیت سایبری** | بدافزارها، فیشینگ، استخراج‌کننده‌های ارز دیجیتال |
| 🙅 **حذف مزاحمت‌ها** | پاپ‌آپ‌های کوکی، ویجت‌های اجتماعی، نوتیفیکیشن‌ها |
| 🔞 **نسخه خانواده** | مسدودسازی سخت‌گیرانه محتوای بزرگسالان |
| 🇮🇷 **بهینه برای ایران** | پوشش کامل شبکه‌های تبلیغاتی بومی |
| 🔄 **آپدیت خودکار** | به‌روزرسانی روزانه بدون نیاز به اقدام شما |

---

## 🔗 لینک‌های اشتراک

*(روی لینک‌ها راست‌کلیک کرده و **Copy Link Address** را بزنید)*

### ۱. نسخه نهایی (Ultimate) - 🏆 پیشنهاد اصلی

شامل تمام تبلیغات جهانی و فارسی، ردیاب‌ها، بدافزارها، کوکی‌ها و مزاحمت‌ها.

```text
https://raw.githubusercontent.com/azadigh/PersianShield/main/persianshield-ultimate.txt
```

### ۲. نسخه ایمن برای خانواده (Family Safe) - 👨‍👩‍👧‍👦

شامل تمام ویژگی‌های نسخه نهایی + **مسدودسازی کامل محتوای بزرگسالان**.

```text
https://raw.githubusercontent.com/azadigh/PersianShield/main/persianshield-family.txt
```

---

## 🛠️ راهنمای نصب و فعال‌سازی

### 🔶 در uBlock Origin (پیشنهادی برای مرورگر)

1. روی آیکون افزونه کلیک کرده و وارد **تنظیمات** (Dashboard / چرخ‌دنده) شوید
2. به تب **Filter lists** بروید
3. به پایین‌ترین بخش یعنی **Custom** اسکرول کنید
4. روی **Import** کلیک کرده و یکی از لینک‌های بالا را Paste کنید
5. روی **Apply changes** کلیک کنید ✅

> 💡 **نکته مهم:** برای جلوگیری از مصرف بیهوده رم و کندی مرورگر، پیشنهاد می‌کنیم لیست‌های پیش‌فرض مثل EasyList و EasyPrivacy را **غیرفعال** کنید، زیرا سپر پارسی تمام آن‌ها را به‌صورت بهینه‌تر در خود دارد.

### 🟢 در AdGuard (ویندوز / مک / اندروید)

1. تنظیمات AdGuard را باز کرده و به بخش **Filters** بروید
2. در تب **Custom filters**، روی **Add custom filter** کلیک کنید
3. لینک اشتراک را وارد کرده، نام آن را "PersianShield" بگذارید و ذخیره کنید

### 🌐 در AdGuard Home / Pi-hole (سطح شبکه و DNS)

از آنجا که این لیست شامل صدها هزار دامنه مسدود شده است، می‌توانید از آن در مسدودکننده‌های سطح شبکه نیز استفاده کنید.

> ⚠️ **توجه:** قوانین ظاهری (Cosmetic) و اسکریپت‌ها در سطح DNS کار نمی‌کنند، اما مسدودسازی دامنه‌های تبلیغاتی و مخرب به‌طور کامل انجام می‌شود.

---

## 📚 منابع و لیست‌های استفاده شده

این پروژه از ادغام هوشمندانه **بیش از ۳۰ منبع معتبر** جهانی و فارسی بهره می‌برد. در ادامه تمام منابع به تفکیک دسته‌بندی آورده شده‌اند:

### 🇮🇷 منابع فارسی (ویژه وب ایران)

این لیست‌ها به‌طور اختصاصی برای شناسایی تبلیغات و ردیاب‌های وب فارسی طراحی شده‌اند:

| نام منبع | لینک | توضیحات |
|:---|:---|:---|
| **PersianBlocker** | [GitHub](https://github.com/MasterKia/PersianBlocker) | جامع‌ترین لیست فارسی برای مسدودسازی تبلیغات و ردیاب‌های ایرانی |
| **uBOPa** | [GitHub](https://github.com/nimasaj/uBOPa) | لیست بهینه‌شده برای وب فارسی با تمرکز بر عملکرد بالا |
| **AdBlock Iran** | [GitHub](https://github.com/farrokhi/adblock-iran) | لیست قدیمی و معتبر برای سایت‌های ایرانی |
| **AdBlockFA** | [GitHub](https://github.com/SlashArash/adblockfa) | فیلترهای فارسی برای تبلیغات بومی |
| **Persian Community List** | [Ideone](https://ideone.com/plain/K452p) | لیست جمع‌آوری شده توسط جامعه کاربران فارسی‌زبان |

### 🌍 منابع جهانی تبلیغات و ردیاب‌ها

| نام منبع | لینک | توضیحات |
|:---|:---|:---|
| **EasyList** | [easylist.to](https://easylist.to/) | اصلی‌ترین لیست مسدودسازی تبلیغات جهانی |
| **EasyPrivacy** | [easylist.to](https://easylist.to/) | مسدودسازی ردیاب‌ها و اسکریپت‌های جاسوسی |
| **Peter Lowe's Ad/Tracking Server List** | [pgl.yoyo.org](https://pgl.yoyo.org/adservers/) | لیست سرورهای تبلیغاتی و ردیابی |
| **AdGuard Base filter** | [AdGuard](https://github.com/AdguardTeam/AdGuardFilters) | فیلتر پایه AdGuard برای تبلیغات |
| **AdGuard Tracking Protection** | [AdGuard](https://github.com/AdguardTeam/AdGuardFilters) | حفاظت در برابر ردیابی |
| **AdGuard Mobile Ads** | [AdGuard](https://github.com/AdguardTeam/AdGuardFilters) | مسدودسازی تبلیغات موبایل |
| **AdGuard Experimental** | [AdGuard](https://github.com/AdguardTeam/AdGuardFilters) | قوانین آزمایشی و پیشرفته |
| **uBlock filters** | [GitHub](https://github.com/uBlockOrigin/uAssets) | فیلترهای اصلی uBlock Origin |
| **uBlock Privacy** | [GitHub](https://github.com/uBlockOrigin/uAssets) | فیلترهای حریم خصوصی uBlock |
| **uBlock Unbreak** | [GitHub](https://github.com/uBlockOrigin/uAssets) | رفع مشکلات سایت‌های شکسته |
| **uBlock Quick fixes** | [GitHub](https://github.com/uBlockOrigin/uAssets) | اصلاحات سریع مشکلات |

### 🙅 منابع حذف مزاحمت‌ها (Annoyances)

| نام منبع | لینک | توضیحات |
|:---|:---|:---|
| **EasyList Cookie List** | [easylist.to](https://easylist.to/) | حذف پاپ‌آپ‌های کوکی و GDPR |
| **Fanboy's Annoyance List** | [easylist.to](https://easylist.to/) | حذف مزاحمت‌های عمومی وب |
| **Fanboy's Social Blocking List** | [easylist.to](https://easylist.to/) | حذف ویجت‌های شبکه‌های اجتماعی |
| **Fanboy's Notifications Blocking** | [easylist.to](https://easylist.to/) | مسدودسازی نوتیفیکیشن‌های مزاحم |
| **AdGuard Annoyances** | [AdGuard](https://github.com/AdguardTeam/AdGuardFilters) | فیلتر مزاحمت‌های AdGuard |
| **AdGuard Social Media** | [AdGuard](https://github.com/AdguardTeam/AdGuardFilters) | حذف ویجت‌های اجتماعی |
| **uBlock Annoyances** | [GitHub](https://github.com/uBlockOrigin/uAssets) | فیلتر مزاحمت‌های uBlock |

### 🛡️ منابع امنیت و بدافزار

| نام منبع | لینک | توضیحات |
|:---|:---|:---|
| **oisd full** | [oisd.nl](https://oisd.nl/) | لیست جامع دامنه‌های تبلیغاتی و مخرب |
| **StevenBlack unified hosts** | [GitHub](https://github.com/StevenBlack/hosts) | لیست یکپارچه میزبان‌های تبلیغاتی و بدافزار |
| **uBlock Badware risks** | [GitHub](https://github.com/uBlockOrigin/uAssets) | شناسایی سایت‌های خطرناک |
| **CoinBlockerLists** | [GitHub](https://github.com/ZeroDot1/CoinBlockerLists) | مسدودسازی استخراج‌کننده‌های ارز دیجیتال |
| **NoCoin** | [GitHub](https://github.com/hoshsadiq/adblock-nocoin-list) | مسدودسازی ماینرهای مرورگری |
| **Dandelion Sprout's Anti-Malware** | [GitHub](https://github.com/DandelionSprout/adfilt) | لیست ضد بدافزار پیشرفته |
| **Spam404** | [GitHub](https://github.com/Spam404/lists) | مسدودسازی دامنه‌های اسپم و فیشینگ |

### 🔞 منابع مسدودسازی محتوای بزرگسالان (فقط نسخه Family)

| نام منبع | لینک | توضیحات |
|:---|:---|:---|
| **oisd NSFW** | [oisd.nl](https://oisd.nl/) | لیست دامنه‌های محتوای بزرگسالان |
| **Chad Mayfield Porn Top1M** | [GitHub](https://github.com/chadmayfield/my-pihole-blocklists) | مسدودسازی سایت‌های پورنوگرافی بر اساس آمار |
| **StevenBlack hosts (porn)** | [GitHub](https://github.com/StevenBlack/hosts) | لیست میزبان‌های محتوای بزرگسالان |

### 📝 قوانین سفارشی (فایل `extra.txt`)

علاوه بر منابع فوق، قوانین دست‌نویس و تست‌شده توسط توسعه‌دهنده نیز از فایل `extra.txt` در همین مخزن خوانده شده و به لیست نهایی اضافه می‌شوند. این قوانین شامل اصلاحات اختصاصی برای سایت‌های فارسی و رفع مشکلات خاص هستند.

---

## 📁 ساختار فایل‌ها

```
PersianShield/
├── .github/
│   └── workflows/
│       └── update-filters.yml    # اسکریپت خودکار به‌روزرسانی
├── merge_filters.py              # اسکریپت اصلی ادغام لیست‌ها
├── extra.txt                     # قوانین سفارشی شما
├── persianshield-ultimate.txt    # خروجی نهایی (بدون پورن)
├── persianshield-family.txt      # خروجی نهایی (با پورن)
├── README.md                     # همین فایل
└── LICENSE                       # مجوز MIT
```

---

## ❓ سوالات متداول

**۱. آیا واقعاً به لیست دیگری نیاز ندارم؟**

خیر. این لیست به‌گونه‌ای طراحی شده که تمام لیست‌های معروف را در خود جای داده است. فعال کردن همزمان آن‌ها فقط باعث کندی مرورگر و تداخل قوانین می‌شود.

**۲. سایتی با این لیست به مشکل برخورده است. چه کنم؟**

لطفاً آدرس سایت و مشکل پیش‌آمده را در بخش [Issues](../../issues) یا کانال تلگرام ما گزارش دهید تا در کمتر از ۲۴ ساعت رفع شود.

**۳. لیست هر چند وقت یکبار آپدیت می‌شود؟**

سرورهای گیت‌هاب هر ۲۴ ساعت یک‌بار تمام منابع را بررسی کرده و لیست نهایی را به‌روزرسانی می‌کنند.

**۴. چرا بعضی سایت‌های فارسی هنوز تبلیغ نشان می‌دهند؟**

ممکن است تبلیغ جدید باشد یا اسکریپت ضد-ادبلاک داشته باشد. لطفاً گزارش دهید تا به `extra.txt` اضافه شود.

**۵. آیا این لیست با مرورگرهای موبایل هم کار می‌کند؟**

بله. با Kiwi Browser، Firefox Android (با uBlock Origin) و AdGuard Android به‌خوبی کار می‌کند.

---

## 🤝 مشارکت

اگر می‌خواهید به این پروژه کمک کنید:

1. **گزارش باگ**: در بخش [Issues](../../issues) مشکل را گزارش دهید
2. **اضافه کردن قوانین**: فایل `extra.txt` را ویرایش کرده و Pull Request بفرستید
3. **ستاره دادن**: با ⭐ دادن به مخزن، از پروژه حمایت کنید

---

## 👨‍💻 توسعه‌دهنده و ارتباط با ما

این پروژه با ❤️ توسط **azadigh** توسعه و نگهداری می‌شود.

- 💻 **گیت‌هاب**: [github.com/azadigh](https://github.com/azadigh)
- 📱 **کانال تلگرام**: [t.me/azadi_tg](https://t.me/azadi_tg)

> اگر از این پروژه راضی هستید، با استار دادن (⭐) به مخزن و اشتراک‌گذاری آن در شبکه‌های اجتماعی، از ما حمایت کنید!

---

## 📄 مجوز

این پروژه تحت مجوز [MIT](LICENSE) منتشر شده است. شما آزادید آن را استفاده، ویرایش و بازنشر کنید، به شرط حفظ اعتبار منابع.

---

## 🙏 قدردانی

از تمام توسعه‌دهندگانی که لیست‌های منبع را ایجاد و نگهداری می‌کنند، صمیمانه سپاسگزاریم. این پروژه بدون زحمات آن‌ها ممکن نبود.

---

<div align="center">
  <sub>ساخته شده با ❤️ و قدرت GitHub Actions | آپدیت خودکار روزانه</sub>
</div>
```
