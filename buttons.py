from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Smartfonlar"),
            KeyboardButton(text="Noutbooklar"),
            KeyboardButton(text="Maishiy texnika"),
        ]
    ],
    resize_keyboard=True
)
smartfonlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Iphone"),
            KeyboardButton(text="Samsung"),
            KeyboardButton(text="RedMi"),
        ],
        [
            KeyboardButton(text="Oppo"),
            KeyboardButton(text="Vivo"),
            KeyboardButton(text="Realme"),
        ],
        [
            KeyboardButton(text="Huawei"),
            KeyboardButton(text="Poco")
        ],
        [
            KeyboardButton(text="Birinchi sahifaqa qaytish")
        ]
    ],
    resize_keyboard=True
)
buyurtma_berish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Buyurtma berish", callback_data="buyurtma"),
        ],
        [
            InlineKeyboardButton(text="Bosh sahifaga qaytish", callback_data="bosh sahifaga qaytish"),
        ]
    ]
)
ortga_1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ortga qaytish")
        ]
    ],
    resize_keyboard=True
)
ortga_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ortga  qaytish")
        ]
    ],
    resize_keyboard=True
)
ortga_3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Oldingi sahifaga qaytish")
        ]
    ],
    resize_keyboard=True
)
ortga_4 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Oldingi  sahifaga qaytish")
        ]
    ],
    resize_keyboard=True
)
ortga_5 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Oldingi sahifaga  qaytish")
        ]
    ],
    resize_keyboard=True
)
ortga_6 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Oldingi  sahifaga  qaytish")
        ]
    ],
    resize_keyboard=True
)


malumot = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon raqam yuborish👇", request_contact=True),
        ]
    ],
    resize_keyboard=True
)
malumot_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Manzil yuborish👇", request_location=True)
        ]
    ],
    resize_keyboard=True
)

menuga_qaytish = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bosh sahifaga qaytish")
        ]
    ],
    resize_keyboard=True
)
qayta_xarid = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Qayta xarid👇")
        ]
    ],
    resize_keyboard=True
)
noutbooklar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ASUS"),
            KeyboardButton(text="H/P")
        ],
        [
            KeyboardButton(text="Lenovo"),
            KeyboardButton(text="MSI")
        ],
        [
            KeyboardButton(text="Birinchi sahifaqa qaytish")
        ]
    ],
    resize_keyboard=True
)
texnika_turi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Televizor"),
            KeyboardButton(text="Muzlatgich"),
        ],
        [
            KeyboardButton(text="Konditsioner"),
            KeyboardButton(text="Kir yuvish mashinasi"),
        ],
        [
            KeyboardButton(text="Bosh sahifaga qaytish")
        ]
    ],
    resize_keyboard=True
)
televizor = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Artel TV"),
            KeyboardButton(text="Toshiba TV")
        ],
        [
            KeyboardButton(text="SONY TV"),
            KeyboardButton(text="Samsung TV")
        ],
        [
            KeyboardButton(text="Orqaga qaytish")
        ]
    ],
    resize_keyboard=True
)
muzlatgich = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Hoffman Muzlatgichi"),
            KeyboardButton(text="Bosch Muzlatgichi")
        ],
        [
            KeyboardButton(text="Shivaki Muzlatgichi"),
            KeyboardButton(text="Goodwell Muzlatgichi")
        ],
        [
            KeyboardButton(text="Orqaga qaytish")
        ]
    ],
    resize_keyboard=True
)
konditsioner = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="LG konditsioneri"),
            KeyboardButton(text="Artel konditsioneri"),
        ],
        [
            KeyboardButton(text="Shivaki konditsioneri"),
            KeyboardButton(text="Panasonic konditsioneri")
        ],
        [
            KeyboardButton(text="Orqaga qaytish")
        ]
    ],
    resize_keyboard=True
)
kir_yuvish_mashinasi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Hoffman"),
            KeyboardButton(text="Goodwell"),
        ],
        [
            KeyboardButton(text="LG"),
            KeyboardButton(text="Bosch")
        ],
        [
            KeyboardButton(text="Orqaga qaytish")
        ]
    ],
    resize_keyboard=True
)

