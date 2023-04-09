from aiogram import executor, types
from aiogram.types import Message, CallbackQuery
from config import dp
from buttons import menu, smartfonlar, buyurtma_berish, ortga_1, malumot, menuga_qaytish, qayta_xarid, malumot_2, \
    noutbooklar, ortga_2, ortga_3, ortga_4,ortga_5,ortga_6,texnika_turi, televizor, muzlatgich, konditsioner, kir_yuvish_mashinasi


@dp.message_handler(commands=['start'])
async def start_1(msg: Message):
    text = f"BIZNING ONLINE ELECTRONIKA MAGAZINIMIZGA XUSH KELIBSIZ!\nBizning magazinda siz ko'p turdagi va istalgan texnikangizni sotib olishingiz mumkin.\nSizni qanday mahsulot qiziqtiradi.👇"
    image = open('foto/logo electro shop.jpg', 'rb')
    await msg.answer_photo(image, caption=text, reply_markup=menu)


@dp.message_handler(commands=["help"])
async def help_1(msg: Message):
    await msg.answer(
        f"Agar sizda qandaydir muammolar paydo bo'lgan bo'lsa bizning admin bilan bog'lanib ularni hal etishingiz mumkin\nAmdin: https://t.me/aaaa_77_01")
    await msg.answer("Agar maummolar xal etilgan bo'lsa qaytadan xaridni boshlashingiz mumkin.👇",
                     reply_markup=qayta_xarid)


@dp.message_handler(commands=['stop'])
async def stop_1(msg: Message):
    text = "Xarid to'xtatildi siz bosh menuga qayttingiz!"
    await msg.answer(text, reply_markup=menu)


@dp.callback_query_handler(text="buyurtma")
async def buyurtma_1(call: CallbackQuery):
    text = f"Buyurtma berish uchun o'z raqamingizni undan so'ng o'z turar joyingizni yuboring:👇"
    await call.message.answer(text, reply_markup=malumot)


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def buyurtma_qabul(msg: Message):
    text = f"Sizning buyurtmangiz muvaffaqiyatli qabul qilindi😊\nBuyurtmangiz tayyor bo'lishi bilan, biz siz bilan bog'lanamiz\nKuningiz hayrli bo'lsin👍"
    await msg.answer(text, reply_markup=menuga_qaytish)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def raqam(msg: Message):
    text = f"Raqamingiz qabul qilindi.\nEndi esa yashash manzilingiz yuboring;👇"
    await msg.answer(text, reply_markup=malumot_2)


@dp.message_handler(text="Smartfonlar")
async def phone_1(msg: Message):
    text = f"Smartfon turini tanlang:👇"
    await msg.answer(text, reply_markup=smartfonlar)


@dp.message_handler(text="Birinchi sahifaqa qaytish")
async def bosh_sahifa(msg: Message):
    text = f"Birinchi sahifaga qayttingiz."
    await msg.answer(text, reply_markup=menu)


@dp.message_handler(text="Bosh sahifaga qaytish")
async def bosh_sahifa_2(msg: Message):
    text = f"Bosh sahifaga qayttingiz."
    await msg.answer(text, reply_markup=menu)


@dp.callback_query_handler(text="bosh sahifaga qaytish")
async def bosh_sahifa_2(call: CallbackQuery):
    text = f"Bosh sahifaga qayttingiz."
    await call.message.answer(text, reply_markup=menu)


@dp.message_handler(text="Qayta xarid👇")
async def qayta(msg: Message):
    text = "Siz qayta xaridni boshladingiz.\nBizni tanlaganingizdan nihoyatta mamnunmiz.👍"
    await msg.answer(text, reply_markup=menu)


@dp.message_handler(text="Iphone")
async def iphone(msg: Message):
    text = f"Smartfon tanlab, buyurtma berishingiz mumkin!😊"
    image = open('iphone/iphone 2.jpeg', 'rb')
    image_2 = open('iphone/iphone 3.jpg', 'rb')
    image_3 = open('iphone/iphone 4.png', 'rb')
    image_4 = open('iphone/iphone 5.jpg', 'rb')
    image_5 = open('iphone/iphone 6.jpg', 'rb')
    text_1 = f"Model Iphone X\nXususiyatlari:\nEkran yangilanish chastotasi	60 Гц\nSIM-karta formati	nano SIM\nSIM-kartalar soni	1\nHimoya darajasi	IP67\nOperatsion tizim versiyasi	iOS 11\nNFC	Bor\nEkran texnologiyasi	OLED\nEkran piksellari o'lchamlari	2436x1125\nEkran tomonlari nisbati	19.5:9\nAloqa standarti	3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900\nKorpus materiali	алюминий и стекло\nBluetooth standarti	5.0\nProtsessor	Apple A11 Bionic\nOld Kamera	7 МП\nOrqa kamera	12 МП, 12 МП\nVazn	174 г\nBatareya quvvati	2716 мА⋅ч\nEkran o'lchami	5.8\nDoimiy xotira hajmi	64 ГБ\nOperativ xotira hajmi	3 ГБ\nBrend	Apple\nNarxi: 3.500.000 so'm"
    text_2 = f"Model  Iphone 11\nXususiyatlari:\nEkran yangilanish chastotasi	60 Гц\nSIM-kartalar soni	2\nSIM-karta formati	nano SIM+eSIM\nHimoya darajasi	IP68\nProtsessor	Apple A13 Bionic\nOperatsion tizim versiyasi	iOS 13\nNFC	Bor\nEkran texnologiyasi	IPS\nEkran piksellari o'lchamlari	1792x828\nEkran tomonlari nisbati	19.5:9\nAloqa standarti	3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900\nKorpus materiali	металл и стекло\nBluetooth standarti	5.0\nOld Kamera	12 МП\nOrqa kamera	12 МП, 12 МП\nVazn	194 г\nBatareya quvvati	3110 мА⋅ч\nEkran o'lchami	6.1\nDoimiy xotira hajmi	64 ГБ\nOperativ xotira hajmi	4 ГБ\nBrend	Apple\nNarxi: 7.900.000 so'm"
    text_3 = f"Model  Iphone 12\nXususiyatlari:\nEkran yangilanish chastotasi 60 Гц\nSIM-karta formati nano SIM+eSIM\nSIM-kartalar soni 2\nHimoya darajasi IP68\nOperatsion tizim versiyasi iOS 14\nNFC Bor\nEkran texnologiyasi OLED\nEkran tomonlari nisbati 19.5:9\nAloqa standarti 3G, 4G LTE, LTE-A, VoLTE, 5G, GSM 900/1800/1900\nKorpus materiali алюминий и стекло\nBluetooth standarti 5.0\nBatareya quvvati 2815 мА⋅ч\nEkran piksellari o'lchamlari 2532x1170\nProtsessor Apple A14 Bionic\nOld Kamera 12 МП\nOrqa kamera 12 МП, 12 МП\nVazn 164 г\nEkran o'lchami 6.1\nDoimiy xotira hajmi 128 ГБ\nOperativ xotira hajmi 4 ГБ\nBrend Apple\nNarxi: 9.900.000 so'm"
    text_4 = f"Model Iphone 13\nXususiyatlari:\nHimoya darajasi	IP68\nBluetooth standarti	5.0\nnProtsessor	Apple A15 Bionic\nOperatsion tizim versiyasi	iOS 15\nAloqa standarti	3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900\nOld Kamera	12 МП\nOrqa kamera	12 МП, 12 МП\nKorpus materiali	алюминий и стекло\nVazn	173 г\nEkran tomonlari nisbati	19.5:9\nEkran piksellari o'lchamlari	2532x1170\nEkran texnologiyasi	OLED\nEkran o'lchami	6.1\nDoimiy xotira hajmi	128 ГБ\nOperativ xotira hajmi	4 ГБ\nBrend	Apple\nNarxi: 10.811.000 so'm"
    text_5 = f"Model Iphone 14\nXususiyatlari:\nHimoya darajasi	IP68\nBluetooth standarti	5.3\nProtsessor	Apple A15 Bionic\nAloqa standarti	3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900\nOld Kamera	12 МП\nOrqa kamera	12 МП, 12 МП\nKorpus materiali	алюминий и стекло\nVazn	172 г\nEkran tomonlari nisbati	19.5:9\nEkran piksellari o'lchamlari	2532x1170\bEkran texnologiyasi	OLED\bEkran o'lchami	6.1\bDoimiy xotira hajmi	128 ГБ\bOperativ xotira hajmi	6 ГБ\bBrend	Apple\nNarxi: 10.610.000 so'm"
    await msg.answer(text, reply_markup=ortga_1)
    await msg.answer_photo(image, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)


@dp.message_handler(text="Samsung")
async def samsung(msg: Message):
    text = f"Smartfon tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('samsung/samsung 1.jpg', 'rb')
    image_2 = open('samsung/samsung 2.jpeg', 'rb')
    image_3 = open('samsung/samsung 3.jpeg', 'rb')
    image_4 = open('samsung/samsung 4.jpeg', 'rb')
    image_5 = open('samsung/samsung 5.jpg', 'rb')
    text_1 = f"Model Samsung Note 10 plus\nXususiyatlari:\nEkran yangilanish chastotasi	60 Гц\nHimoya darajasi	IP68\nSIM-karta formati	nano SIM\nSIM-kartalar soni	2\nNFC	Bor\nXotira kartasi sloti	Есть\nAloqa standarti	3G, 4G LTE, LTE-A, GSM 900/1800/1900\nKorpus materiali	металл и стекло\nBluetooth standarti	5.0\nOperatsion tizim versiyasi	Android 10\nProtsessor	Samsung Exynos 9825\nOld Kamera	10 МП\nOrqa kamera	12 МП, 16 МП, 12 МП\nVazn	196 г\nBatareya quvvati	4300 мА⋅ч\nEkran tomonlari nisbati	19:9\nEkran texnologiyasi	AMOLED\nEkran piksellari o'lchamlari	3040x1440\nEkran o'lchami	6.8\nDoimiy xotira hajmi	256 ГБ\nOperativ xotira hajmi	12 ГБ\nBrend	Samsung\nNarxi: 4.500.000 so'm"
    text_2 = f"Model Samsung Note 20 Ultra\nXususiyatlari:\nEkran yangilanish chastotasi	60 Гц\nSIM-karta formati	nano SIM\nSIM-kartalar soni	2\nHimoya darajasi	IP68\nOperatsion tizim versiyasi	Android 10\nXotira kartasi sloti	Есть\nNFC	Bor\nAloqa standarti	3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900\nEkran tomonlari nisbati	20:9\nKorpus materiali	металл и стекло\nBluetooth standarti	5.0\nProtsessor	Samsung Exynos 990\nOld Kamera	10 МП\nOrqa kamera	64 МП, 12 МП, 12 МП\nVazn	195 г\nBatareya quvvati	4300 мА⋅ч\nEkran piksellari o'lchamlari	2400x1080\nEkran texnologiyasi	Super AMOLED\nEkran o'lchami	6.7\nDoimiy xotira hajmi	256 ГБ\nOperativ xotira hajmi	8 ГБ\nBrend	Samsung\nNarxi: 5.500.000 so'm"
    text_3 = f"Model S20 Ultra\nXususiyatlari:\nEkran yangilanish chastotasi	120 Гц\nSIM-karta formati	nano SIM\nSIM-kartalar soni	2\nHimoya darajasi	IP68\nOperatsion tizim versiyasi	Android 10\nEkran texnologiyasi	AMOLED\nEkran tomonlari nisbati	20:9\nNFC	Bor\nXotira kartasi sloti	Есть\nAloqa standarti	3G, 4G LTE, 5G, GSM 900/1800/1900\nKorpus materiali	металл и стекло\nBluetooth standarti	5.0\nEkran piksellari o'lchamlari	3200x1440\nProtsessor	Samsung Exynos 990\nOld Kamera	40 МП\nOrqa kamera	108 МП, 48 МП, 12 МП\nVazn	220 г\nBatareya quvvati	5000 мА⋅ч\nEkran o'lchami	6.9\nDoimiy xotira hajmi	128 ГБ\nOperativ xotira hajmi	12 ГБ\nBrend	Samsung\nNarxi: 10.201.000 so'm"
    text_4 = f"Model Samsung S21 Ultra\nXususiyatlari:\nEkran yangilanish chastotasi	120 Гц\nSIM-karta formati	nano SIM+eSIM\nSIM-kartalar soni	2\nHimoya darajasi	IP68\nNFC	Bor\nKorpus materiali	алюминий и стекло\nBluetooth standarti	5.2\nAloqa standarti	3G, 4G LTE, LTE-A, VoLTE, 5G, GSM 900/1800/1900\nOperatsion tizim versiyasi	Android 11\nProtsessor	Samsung Exynos 2100\nOld Kamera	40 МП\nOrqa kamera	108 МП, 12 МП, 10 МП, 10 МП\nVazn	228 г\nBatareya quvvati	5000 мА⋅ч\nEkran tomonlari nisbati	20:9\nEkran piksellari o'lchamlari	3200x1440\nEkran o'lchami	6.8\nEkran texnologiyasi	Dynamic AMOLED 2X\nDoimiy xotira hajmi	256 ГБ\nOperativ xotira hajmi	12 ГБ\nBrend	Samsung\nNarxi: 13.512.500 so'm"
    text_5 = f"Model Samsung S22 Ultra\nXususiyatlari:\nEkran yangilanish chastotasi	120 Гц\nSIM-karta formati	nano SIM+eSIM\nSIM-kartalar soni	2\nHimoya darajasi	IP68\nNFC	Bor\nBluetooth standarti	5.2\nAloqa standarti	3G, 4G LTE, LTE-A, VoLTE, 5G, GSM 900/1800/1900\nProtsessor	Samsung Exynos 2200\nOld Kamera	40 МП\nOrqa kamera	108 МП, 12 МП, 10 МП, 10 МП\nVazn	228 г\nBatareya quvvati	5000 мА⋅ч\nEkran tomonlari nisbati	19:9\nEkran piksellari o'lchamlari	3088x1440\nEkran o'lchami	6.8\nEkran texnologiyasi	Dynamic AMOLED 2X\nDoimiy xotira hajmi	512 ГБ\nOperativ xotira hajmi	12 ГБ\nBrend	Samsung\nNarxi: 12.825.000 so'm"
    await msg.answer(text, reply_markup=ortga_1)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)


@dp.message_handler(text="Ortga qaytish")
async def ortga(msg: Message):
    text = f"Oldingi sahifaga qayttingiz."
    await msg.answer(text, reply_markup=smartfonlar)


@dp.message_handler(text="Ortga  qaytish")
async def orqaga_qaytish(msg: Message):
    text = f"Oldingi sahifaga qayttingiz."
    await msg.answer(text, reply_markup=noutbooklar)


@dp.message_handler(text="Orqaga qaytish")
async def orqaga_qaytish(msg: Message):
    text = f"Oldingi sahifaga qayttingiz"
    await msg.answer(text, reply_markup=texnika_turi)


@dp.message_handler(text="Oldingi sahifaga qaytish")
async def orqa_3(msg: Message):
    text = f"Oldingi sahifaga qayttingiz"
    await msg.answer(text, reply_markup=televizor)

@dp.message_handler(text="Oldingi  sahifaga qaytish")
async def orqa_3(msg: Message):
    text = f"Oldingi sahifaga qayttingiz"
    await msg.answer(text, reply_markup=muzlatgich)

@dp.message_handler(text="Oldingi sahifaga  qaytish")
async def orqa_3(msg: Message):
    text = f"Oldingi sahifaga qayttingiz"
    await msg.answer(text, reply_markup=konditsioner)

@dp.message_handler(text="Oldingi  sahifaga  qaytish")
async def orqa_3(msg: Message):
    text = f"Oldingi sahifaga qayttingiz"
    await msg.answer(text, reply_markup=kir_yuvish_mashinasi)


@dp.message_handler(text="RedMi")
async def redmi(msg: Message):
    text = f"Smartfon tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('redmi/redmi 1.png', 'rb')
    image_2 = open('redmi/redmi 2.jpeg', 'rb')
    image_3 = open('redmi/redmi 3.jpg', 'rb')
    image_4 = open('redmi/redmi 4.jpg', 'rb')
    image_5 = open('redmi/redmi 5.jpg', 'rb')
    text_1 = f"Model RedMi Note 8\nXususiyatlari:\nEkran yangilanish chastotasi	60 Гц\nSIM-karta formati	nano SIM\nSIM-kartalar soni	2\nOperatsion tizim versiyasi	Android 9.0\nXotira kartasi sloti	Bor\nEkran texnologiyasi	IPS\nEkran tomonlari nisbati	19.5:9\nAloqa standarti	3G, 4G LTE, VoLTE, GSM 900/1800/1900\nKorpus materiali	стекло и пластик\nBluetooth standarti	4.2\nEkran piksellari o'lchamlari	2340x1080\nProtsessor	Qualcomm Snapdragon 665\nOld Kamera	13 МП\nOrqa kamera	48 МП, 8 МП, 2 МП, 2 МП\nVazn	190 г\nBatareya quvvati	4000 мА⋅ч\nEkran o'lchami	6.3\nDoimiy xotira hajmi	64 ГБ\nOperativ xotira hajmi	4 ГБ\nBrend	Xiaomi\nNarxi: 2.500.000 so'm"
    text_2 = f"Model RedMi Note 9\nXususiyatlari:\nEkran yangilanish chastotasi	60 Гц\nSIM-karta formati	nano SIM\nSIM-kartalar soni	2\nOperatsion tizim versiyasi	Android 10\nXotira kartasi sloti	Bor\nEkran texnologiyasi	IPS\nEkran piksellari o'lchamlari	2340x1080\nEkran tomonlari nisbati	19.5:9\nAloqa standarti	3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900\nKorpus materiali	стекло и пластик\nBluetooth standarti	5.0\nOld Kamera	13 МП\nOrqa kamera	48 МП, 8 МП, 2 МП, 2 МП\nVazn	199 г\nBatareya quvvati	5020 мА⋅ч\nEkran o'lchami	6.53\nDoimiy xotira hajmi	128 ГБ\nOperativ xotira hajmi	4 ГБ\nBrend	Xiaomi\nNarxi: 2.700.000 so'm"
    text_3 = f"Model RedMi Note 10\nXususiyatlari:\nEkran yangilanish chastotasi	60 Гц\nSIM-karta formati	nano SIM\nSIM-kartalar soni	2\nHimoya darajasi	IP53\nOperatsion tizim versiyasi	Android 11\nXotira kartasi sloti	Bor\nAloqa standarti	3G, 4G LTE, VoLTE, GSM 900/1800/1900\nKorpus materiali	стекло и пластик\nBluetooth standarti	5.0\nOld Kamera	13 МП\nOrqa kamera	48 МП, 8 МП, 2 МП, 2 МП\nVazn	179 г\nBatareya quvvati	5000 мА⋅ч\nEkran piksellari o'lchamlari	2400x1080\nEkran tomonlari nisbati	20:9\nEkran texnologiyasi	Super AMOLED\nEkran o'lchami	6.43\nDoimiy xotira hajmi	64 ГБ\nOperativ xotira hajmi	4 ГБ\nBrend	Xiaomi\nNarxi: 2.815.000 so'm"
    text_4 = f"Model RedMi Note 11\nXususiyatlari:\nEkran yangilanish chastotasi	90 Гц\nProtsessor	Qualcomm Snapdragon 680\nOld Kamera	13 МП\nSIM-karta formati	nano SIM\nSIM-kartalar soni	2\nOperatsion tizim versiyasi	Android 11\nXotira kartasi sloti	Bor\nAloqa standarti	3G, 4G LTE, GSM 900/1800\nBluetooth standarti	5.0\nOrqa kamera	50 МП, 8 МП, 2 МП, 2 МП\nVazn	179 г\nBatareya quvvati	5000 мА⋅ч\nEkran piksellari o'lchamlari	2400x1080\nEkran tomonlari nisbati	20:9\nEkran texnologiyasi	AMOLED\nEkran o'lchami	6.43\nDoimiy xotira hajmi	128 ГБ\nOperativ xotira hajmi	6 ГБ\nBrend	Xiaomi\nNarxi: 3.200.000 so'm"
    text_5 = f"Model RedMi Note 12\nXususiyatlari:\nHimoya darajasi IP53\nNFC Bor\nEkran yangilanish chastotasi 120 Гц\nProtsessor MediaTek Dimensity 1080\nOld Kamera 16 МП\nSIM-karta formati nano SIM\nSIM-kartalar soni 2\nOperatsion tizim versiyasi Android 12\nAloqa standarti 3G, 4G LTE, 5G\nBluetooth standarti 5.2\nOrqa kamera 50 МП, 8 МП, 2 МП\nVazn 187 г\nBatareya quvvati 5000 мА⋅ч\nEkran piksellari o'lchamlari 2400x1080\nEkran tomonlari nisbati 20:9\nEkran texnologiyasi OLED\nEkran o'lchami 6.67\nDoimiy xotira hajmi 256 ГБ\nOperativ xotira hajmi 8 ГБ\nBrend Xiaomi\nNarxi: 3.500.000 so'm"
    await msg.answer(text, reply_markup=ortga_1)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)


@dp.message_handler(text="Oppo")
async def oppo(msg: Message):
    text = f"Smartfon tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('oppo/oppo 1.png', 'rb')
    image_2 = open('oppo/oppo 2.jpg', 'rb')
    image_3 = open('oppo/oppo 3.png', 'rb')
    image_4 = open('oppo/oppo 4.jpg', 'rb')
    image_5 = open('oppo/oppo 5.jpeg', 'rb')
    text_1 = f"Model Oppo A94\nXususiyatlari:\nDispley: 6.43 AMOLED - 1080 x 2400\nChip: MediaTek Dimensity 800U 5G\nKamera: 4 (48 MP + 8 MP + 2 MP + 2 MP)\nBatareya: 4310 мАч\nOperatsoin Tizim: Android 11\nVazn: 173 г.\nNarxi: 3.367.000 so'm"
    text_2 = f"Model Oppo RENO 5\nXususiyatlari:\nEkran yangilanish chastotasi	60 Гц\nSIM-karta formati	nano SIM\nSIM-kartalar soni	2\nXotira kartasi sloti	Bor\nProtsessor	MediaTek Helio P65\nOperatsion tizim versiyasi	Android 11\nAloqa standarti	3G, 4G LTE, LTE-A, GSM 900/1800/1900\nNFC	Bor\nBluetooth standarti	5.1\nOld Kamera	32 МП\nOrqa kamera	48 МП, 8 МП, 2 МП, 2 МП\nVazn	172 г\nBatareya quvvati	4310 мА⋅ч\nKorpus materiali	пластик\nEkran piksellari o'lchamlari	2400x1080\nEkran tomonlari nisbati	20:9\nEkran texnologiyasi	AMOLED\nEkran o'lchami	6.43\nDoimiy xotira hajmi	128 ГБ\nOperativ xotira hajmi	8 ГБ\nBrend	OPPO\nNarxi: 3.616.000 so'm"
    text_3 = f"Model Oppo F17 pro\nXususiyatlari:\nDispley: 6.43 Super AMOLED - 1080 x 2400\nChip: Mediatek Helio P95\nKamera: 4 (48 MP + 8 MP + 2 MP + 2 MP)\nBatareya: 4000 мАч\nOperatsion Tizim: Android 10\nVazn: 164 г.\nNarxi: 3.370.500 so'm"
    text_4 = f"Model Oppo A54\nXususiyatlari:\nEkran yangilanish chastotasi	60 Гц\nSIM-karta formati	nano SIM\nSIM-kartalar soni	2\nProtsessor	MediaTek Helio P35\nOperatsion tizim versiyasi	Android 10\nAloqa standarti	3G, 4G LTE, GSM 900/1800/1900\nXotira kartasi sloti	Bor\nNFC	Bor\nBluetooth standarti	5.0\nOld Kamera	16 МП\nOrqa kamera	13 МП, 2 МП, 2 МП\nVazn	192 г\nBatareya quvvati	5000 мА⋅ч\nEkran piksellari o'lchamlari	1600x720\nEkran tomonlari nisbati	20:9\nEkran o'lchami	6.51\nDoimiy xotira hajmi	64 ГБ\nOperativ xotira hajmi	4 ГБ\nBrend	OPPO\nNarxi: 3.180.000 so'm"
    text_5 = f"Model Oppo A5S\nXususiyatlari:\nOperativ xotira hajmi	3 ГБ\nDoimiy xotira hajmi	32 ГБ\nEkran o'lchami	6.2\nEkran texnologiyasi	IPS\nEkran piksellari o'lchamlari	1520x720\nEkran tomonlari nisbati	19:9\nBatareya quvvati	4230 мА⋅ч\nVazn	170 г\nOrqa kamera	13 МП, 2 МП\nOld Kamera	8 МП\nOperatsion tizim versiyasi	Android 8.1\nProtsessor	MediaTek Helio P35\nAloqa standarti	3G, 4G LTE, GSM 900/1800/1900\nBluetooth standarti	4.2\nKorpus materiali	пластик\nXotira kartasi sloti	Есть\nSIM-kartalar soni	2\nSIM-karta formati	nano SIM\nBrend	OPPO\nNarxi: 1.789.700 so'm"
    await msg.answer(text, reply_markup=ortga_1)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)


@dp.message_handler(text="Realme")
async def realmi(msg: Message):
    text = f"Smartfon tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('realmi/realmi1.jpg', 'rb')
    image_2 = open('realmi/realmi 2.png', 'rb')
    image_3 = open('realmi/realmi 3.jpg', 'rb')
    image_4 = open('realmi/realmi 4.jpg', 'rb')
    image_5 = open('realmi/realmi 5.jpg', 'rb')
    text_1 = f"Model Realme 6\nXususiyatlari:\nEkran yangilanish chastotasi	90 Гц\nSIM-karta formati	nano SIM\nSIM-kartalar soni	2\nNFC	Bor\nOperatsion tizim versiyasi	Android 10\nXotira kartasi sloti	Bor\nEkran texnologiyasi	IPS\nEkran tomonlari nisbati	20:9\nAloqa standarti	3G, 4G LTE, VoLTE, GSM 900/1800/1900\nKorpus materiali	пластик\nBluetooth standarti	5.0\nBrend	Realme\nOperativ xotira hajmi	4 ГБ\nDoimiy xotira hajmi	128 ГБ\nEkran o'lchami	6.5\nBatareya quvvati	4300 мА⋅ч\nVazn	191 г\nOrqa kamera	64 МП, 8 МП, 2 МП, 2 МП\nOld Kamera	16 МП\nProtsessor	MediaTek Helio G90T\nEkran piksellari o'lchamlari	2400x1080\nNarxi: 2.893.000 so'm"
    text_2 = f"Model Realme C3\nXususiyatlari:\nEkran yangilanish chastotasi	60 Гц\nSIM-karta formati	nano SIM\nSIM-kartalar soni	2\nNFC	Bor\nOperatsion tizim versiyasi	Android 10\nXotira kartasi maksimal hajmi	256ГБ\nXotira kartasi sloti	Bor\nEkran texnologiyasi	IPS\nEkran tomonlari nisbati	20:9\nAloqa standarti	3G, 4G LTE, GSM 900/1800/1900\nKorpus materiali	пластик\nBluetooth standarti	5.0\nEkran piksellari o'lchamlari	1600x720\nProtsessor	MediaTek Helio G70\nOld Kamera	2 МП\nOrqa kamera	12 МП, 2 МП, 2 МП\nVazn	195 г\nBatareya quvvati	5000 мА⋅ч\nEkran o'lchami	6.52\nDoimiy xotira hajmi	64 ГБ\nOperativ xotira hajmi	3 ГБ\nBrend	Realme\nNarxi: 1.490.000 so'm"
    text_3 = f"Model Realme C11\nXususiyatlari:\nEkran yangilanish chastotasi	60 Гц\nSIM-kartalar soni	2\nOperatsion tizim versiyasi	Android 10\nXotira kartasi maksimal hajmi	256ГБ\nXotira kartasi sloti	Bor\nEkran tomonlari nisbati	20:9\nEkran texnologiyasi	IPS\nAloqa standarti	3G, 4G LTE, LTE-A, VoLTE, GSM 900/1800/1900\nKorpus materiali	пластик\nBluetooth standarti	5.0\nEkran piksellari o'lchamlari	1600x720\nProtsessor	MediaTek Helio G35\nOld Kamera	5 МП\nOrqa kamera	13 МП, 2 МП\nVazn	196 г\nBatareya quvvati	5000 мА⋅ч\nEkran o'lchami	6.5\nDoimiy xotira hajmi	32 ГБ\nOperativ xotira hajmi	2 ГБ\nBrend	Realme\nNarxi: 1.411.000 so'm"
    text_4 = f"Model Realme 7i\nXususiyatlari:\nEkran yangilanish chastotasi	90 Гц\nSIM-kartalar soni	2\nXotira kartasi sloti	Bor\nKorpus materiali	пластик\nNFC	Bor\nBluetooth standarti	5.0\nAloqa standarti	3G, 4G LTE, LTE-A, GSM 900/1800/1900\nOperatsion tizim versiyasi	Android 10\nProtsessor	Qualcomm Snapdragon 662\nOld Kamera	16 МП\nOrqa kamera	64 МП, 4 МП, 2 МП\nVazn	188 г\nBatareya quvvati	5000 мА⋅ч\nEkran piksellari o'lchamlari	1600x720\nEkran tomonlari nisbati	20:9\nEkran o'lchami	6.5\nEkran texnologiyasi	IPS\nDoimiy xotira hajmi	128 ГБ\nOperativ xotira hajmi	4 ГБ\nBrend	Realme\nNarxi: 2.879.000 so'm"
    text_5 = f"Model Realme 8 pro\nXususiyatlari:\nEkran yangilanish chastotasi 60 Гц\nSIM-karta formati nano SIM\nSIM-kartalar soni 2\nXotira kartasi sloti Bor\nProtsessor Qualcomm Snapdragon 720G\nOperatsion tizim versiyasi Android 11\nAloqa standarti 3G, 4G LTE, GSM 900/1800/1900\nNFC Bor\nBluetooth standarti 5.0\nOld Kamera 16 МП\nOrqa kamera 108 МП, 8 МП, 2 МП, 2 МП\nVazn 176 г\nBatareya quvvati 4500 мА⋅ч\nEkran piksellari o'lchamlari 2400x1080\nEkran tomonlari nisbati 20:9\nEkran texnologiyasi Super AMOLED\nEkran o'lchami 6.4\nDoimiy xotira hajmi 128 ГБ\nOperativ xotira hajmi 6 ГБ\nBrend Realme\nNarxi: 3.420.000 so'm"
    await msg.answer(text, reply_markup=ortga_1)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)


@dp.message_handler(text="Huawei")
async def huawei(msg: Message):
    text = f"Smartfon tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('huawei/huawei 1.jpg', 'rb')
    image_2 = open('huawei/huawei 2.jpg', 'rb')
    image_3 = open('huawei/huawei 3.jpg', 'rb')
    image_4 = open('huawei/huawei 4.jpg', 'rb')
    image_5 = open('huawei/huawei 5.png', 'rb')
    text_1 = f"Model Huawei P50 pro\nXususiyatlari:\nEkran yangilanish chastotasi	120 Гц\nSIM-karta formati	nano SIM+eSIM\nSIM-kartalar soni	2\nHimoya darajasi	IP68\nXotira kartasi sloti	Bor\nEkran texnologiyasi	OLED\nEkran tomonlari nisbati	19.5:9\nAloqa standarti	3G, 4G LTE\nKorpus materiali	алюминий и стекло\nNFC	Bor\nBluetooth standarti	5.2\nEkran piksellari o'lchamlari	2700x1228\nProtsessor	Qualcomm Snapdragon 888\nOld Kamera	13 МП\nOrqa kamera	50 МП, 13 МП, 64 МП\nVazn	195 г\nBatareya quvvati	4360 мА⋅ч\nEkran o'lchami	6.6\nDoimiy xotira hajmi	256 ГБ\nOperativ xotira hajmi	8 ГБ\nBrend	Huawei\nNarxi: 9.699.000 so'm"
    text_2 = f"Model Huawei Nova 10 pro\nXususiyatlari:\nOperatsion tizim versiyasi HarmonyOS 2\nEkran yangilanish chastotasi 120 Гц\nSIM-karta formati nano SIM\nSIM-kartalar soni 2\nProtsessor Qualcomm Snapdragon 778G\nAloqa standarti 3G, 4G LTE\nNFC Bor\nBluetooth standarti 5.2\nOld Kamera 60 МП\nOrqa kamera 50 МП, 8 МП, 2 МП\nVazn 168 г\nBatareya quvvati 4000 мА⋅ч\nEkran piksellari o'lchamlari 2400x1080\nEkran texnologiyasi OLED\nEkran o'lchami 6.67\nDoimiy xotira hajmi 128 ГБ\nOperativ xotira hajmi 8 ГБ\nBrend Huawei\nNarxi: 7.560.000 so'm"
    text_3 = f"Model Huawei Mate XS 2\nXususiyatlari:\nQualcomm SM8350 Snapdragon 888 4G protsessori – 8 yadroli \nAndroid 11 operatsion tizimi, EMUI 12 grafik qobig‘i\nBuklama AMOLED displey – 7,8″, 2200×2480, 424 ppi, 8:9, 120 Gs\nDispley yopilgan holatida – 6,5″, 1176×2480, 19:9\nTezkor xotira 8 GB, ichki xotira 512 GB, UFS 3.1\nmicroSD karta uyachasi yo‘q\nNanoSIM-karta qabul qiladi (2 ta)\nQo‘llanuvchi uyali tarmoqlar: 2G GSM, 3G WCDMA, 4G LTE FDD, 4G LTE TDD\nBluetooth 5.2, A2DP, LE\nNFC\nKameralari: 50 MP + 13 MP \nOld kamera 10,7 MP\nAkkumulyatori 4600 mA/soatlik, tezkor quvvatlash – 66 Vt\nO’lchami 157×139×5,4 mm, yopilgan holatida – 157×76×11,1 mm\nVazni 255/257 g\nNarxi: 19.769.000 so'm"
    text_4 = f"Model Huawei P20\nXususiyatlari:\nTezkor xotira hajmi 4 GB\nDoimiy xotira hajmi 128GB\nVideoprotsessor Mali-G72 MP12\nProtsessor yadrolari soni 8\nProtsessor Hisilicon Kirin 970\nBatareya turi Li-Po\nAkkumulyator sig’imi 3400 mAh\nOld kamera 24 MP\nAsosiy kamera 12MP+20MP\nDispley turi LTPS IPS LCD\nEkran o’lchami 1080 x 2240\nDiagonal 5.8\nNarxi: 1.000.000 so'm"
    text_5 = f"Model Huawei P30\nXususiyatlari:\nBrend	Huawei\nOperativ xotira hajmi	8 ГБ\nDoimiy xotira hajmi	256 ГБ\nEkran o'lchami	6.47\nBatareya quvvati	4200 мА⋅ч\nVazn	192 г\nOrqa kamera	40 МП, 20 МП, 8 МП\nOld Kamera	32 МП\nProtsessor	HiSilicon Kirin 980\nEkran piksellari o'lchamlari	2340x1080\nOperatsion tizim versiyasi	Android 9.0\nEkran texnologiyasi	OLED\nBluetooth standarti	5.0\nKorpus materiali	металл и стекло\nAloqa standarti	3G, 4G LTE, LTE-A, GSM 900/1800/1900\nXotira kartasi sloti	Bor\nNFC	Bor\nHimoya darajasi	IP53\nSIM-kartalar soni	2\nSIM-karta formati	nano SIM\nNarxi: 3.177.900 so'm"
    await msg.answer(text, reply_markup=ortga_1)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)


@dp.message_handler(text="Poco")
async def poco(msg: Message):
    text = f"Smartfon tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('poco/poco 1.jpg', 'rb')
    image_2 = open('poco/poco 2.jpg', 'rb')
    image_3 = open('poco/poco 3.jpg', 'rb')
    image_4 = open('poco/poco 4.jpg', 'rb')
    image_5 = open('poco/poco 5.jpg', 'rb')
    text_1 = f"Model Poco X3\nXususiyatlari:\nEkran yangilanish chastotasi	120 Гц\nSIM-kartalar soni	2\nSIM-karta formati	nano SIM\nHimoya darajasi	IP53\nNFC	Bor\nXotira kartasi maksimal hajmi	256ГБ\nXotira kartasi sloti	Bor\nKorpus materiali	пластик\nBluetooth standarti	5.1\nAloqa standarti	3G, 4G LTE, VoLTE, GSM 900/1800/1900\nEkran tomonlari nisbati	20:9\nOperatsion tizim versiyasi	Android 10\nEkran texnologiyasi	IPS\nEkran piksellari o'lchamlari	2400x1080\nProtsessor	Qualcomm Snapdragon 732G\nOld Kamera	20 МП\nOrqa kamera	64 МП, 13 МП, 2 МП\nVazn	215 г\nBatareya quvvati	5160 мА⋅ч\nEkran o'lchami	6.67\nDoimiy xotira hajmi	128 ГБ\nOperativ xotira hajmi	6 ГБ\nBrend	Xiaomi\nNarxi: 2.693.000 so'm"
    text_2 = f"Model Poco M3\nXususiyatlari:\nEkran yangilanish chastotasi	60 Гц\nSIM-karta formati	nano SIM\nSIM-kartalar soni	2\nXotira kartasi maksimal hajmi	512ГБ\nXotira kartasi sloti	Bor\nKorpus materiali	пластик\nBluetooth standarti	5.0\nAloqa standarti	3G, 4G LTE, GSM 900/1800/1900\nProtsessor	Qualcomm Snapdragon 662\nOperatsion tizim versiyasi	Android 10\nOld Kamera	8 МП\nOrqa kamera	48 МП, 2 МП, 2 МП\nVazn	198 г\nBatareya quvvati	6000 мА⋅ч\nEkran tomonlari nisbati	19.5:9\nEkran piksellari o'lchamlari	2340x1080\nEkran texnologiyasi	IPS\nEkran o'lchami	6.53\nDoimiy xotira hajmi	128 ГБ\nOperativ xotira hajmi	4 ГБ\nBrend	Xiaomi\nNarxi: 2.518.000 so'm"
    text_3 = f"Model Poco F3\nXususiyatlari:\nEkran yangilanish chastotasi	120 Гц\nSIM-karta formati	nano SIM\nSIM-kartalar soni	2\nOperatsion tizim versiyasi	Android 11\nAloqa standarti	3G, 4G LTE, VoLTE, 5G, GSM 900/1800/1900\nNFC	Bor\nBluetooth standarti	5.1\nOld Kamera	20 МП\nOrqa kamera	48 МП, 8 МП, 5 МП\nVazn	196 г\nBatareya quvvati	4520 мА⋅ч\nKorpus materiali	металл и стекло\nEkran piksellari o'lchamlari	2400x1080\nEkran tomonlari nisbati	20:9\nEkran texnologiyasi	AMOLED\nEkran o'lchami	6.67\nProtsessor	Qualcomm Snapdragon 870 5G\nDoimiy xotira hajmi	256 ГБ\nOperativ xotira hajmi	8 ГБ\nBrend	Xiaomi\nNarxi: 4.122.000 so'm"
    text_4 = f"Model Poco X5\nXususiyatlari:\nEkran yangilanish chastotasi 120 Гц\nProtsessor Qualcomm Snapdragon 778G 5G\nSIM-karta formati nano SIM\nSIM-kartalar soni 2\nAloqa standarti 3G, 4G LTE, 5G\nNFC Bor\nBluetooth standarti 5.2\nOld Kamera 16 МП\nOrqa kamera 108 МП, 8 МП, 2 МП\nVazn 181 г\nBatareya quvvati 5000 мА⋅ч\nEkran piksellari o'lchamlari 2400x1080\nEkran tomonlari nisbati 20:9\nEkran texnologiyasi AMOLED\nEkran o'lchami 6.67\nDoimiy xotira hajmi 256 ГБ\nOperativ xotira hajmi 8 ГБ\nBrend Xiaomi\nNarxi: 4.000.000 so'm"
    text_5 = f"Model Poco X3 pro\nXususiyatlari:\nEkran yangilanish chastotasi	120 Гц\nSIM-karta formati	nano SIM\nSIM-kartalar soni	2\nHimoya darajasi	IP53\nOperatsion tizim versiyasi	Android 11\nAloqa standarti	3G, 4G LTE, VoLTE, GSM 900/1800/1900\nXotira kartasi maksimal hajmi	1024ГБ\nXotira kartasi sloti	Есть\nNFC	Bor\nBluetooth standarti	5.0\nOld Kamera	20 МП\nOrqa kamera	48 МП, 8 МП, 2 МП, 2 МП\nVazn	215 г\nBatareya quvvati	5160 мА⋅ч\nKorpus materiali	пластик\nEkran piksellari o'lchamlari	2400x1080\nEkran tomonlari nisbati	20:9\nEkran texnologiyasi	IPS\nEkran o'lchami	6.67\nDoimiy xotira hajmi	256 ГБ\nOperativ xotira hajmi	8 ГБ\nBrend	Xiaomi\nNarxi: 2.287.000 so'm"
    await msg.answer(text, reply_markup=ortga_1)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)


@dp.message_handler(text="Vivo")
async def vivo(msg: Message):
    text = f"Smartfon tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('phone vivo/vivo 1.jpg', 'rb')
    image_2 = open('phone vivo/vivo 2.jpg', 'rb')
    image_3 = open('phone vivo/vivo 3.png', 'rb')
    image_4 = open('phone vivo/vivo 4.png', 'rb')
    image_5 = open('phone vivo/vivo 5.jpg', 'rb')
    text_1 = f"Model Vivo Y12\nXususiyatlari:\nBrend	Vivo\nOperativ xotira hajmi	3 ГБ\nDoimiy xotira hajmi	64 ГБ\nEkran o'lchami	6.35\nBatareya quvvati	5000 мА⋅ч\nVazn	190 г\nOrqa kamera	13 МП, 8 МП, 2 МП\nOld Kamera	8 МП\nOperatsion tizim versiyasi	Android 9.0\nProtsessor	MediaTek Helio P22\nAloqa standarti	3G, 4G LTE, GSM 900/1800/1900\nEkran piksellari o'lchamlari	1544x720\nEkran tomonlari nisbati	19:9\nBluetooth standarti	5.0\nEkran texnologiyasi	IPS\nKorpus materiali	пластик\nXotira kartasi sloti	Bor\nSIM-kartalar soni	2\nSIM-karta formati	nano SIM\nNarxi: 1.100.000 so'm"
    text_2 = f"Model Vivo Y15\nXususiyatlari:\nEkran yangilanish chastotasi	60 Гц\nXotira kartasi sloti	Bor\nSIM-karta formati	nano SIM\nSIM-kartalar soni	2\nKorpus materiali	пластик\nBluetooth standarti	5.0\nAloqa standarti	3G, 4G LTE\nOperatsion tizim versiyasi	Android 11\nProtsessor	MediaTek Helio P35\nOld Kamera	8 МП\nOrqa kamera	13 МП, 2 МП\nBatareya quvvati	5000 мА⋅ч\nEkran tomonlari nisbati	20:9\nEkran piksellari o'lchamlari	1600x720\nEkran o'lchami	6.51\nDoimiy xotira hajmi	32 ГБ\nOperativ xotira hajmi	3 ГБ\nBrend	Vivo\nNarxi: 2.110.000 so'm"
    text_3 = f"Model Vivo Y17\nXususiyatlari:\nProtsessor MT6765\nOperativ xotira 4 ГБ\nXotira 64 ГБ\nBatareya hajmi 5000 мА·ч\nOperatsion sistema Funtouch OS 9 (на базе Android 9.0)\nNarxi: 1.200.000 so'm"
    text_4 = f"Model Vivo Y91\nXususiyatlari:\nBrend Vivo\nOperativ xotira hajmi 2 ГБ\nDoimiy xotira hajmi 32 ГБ\nEkran o'lchami 6.22\nEkran texnologiyasi IPS\bEkran piksellari o'lchamlari 1520x720\nEkran tomonlari nisbati 19:9\nBatareya quvvati 4030 мА⋅ч\nVazn 164 г\nOrqa kamera 13 МП\nOld Kamera 5 МП\nOperatsion tizim versiyasi Android 8.1\nProtsessor MediaTek Helio P22\nAloqa standarti 3G, 4G LTE, VoLTE, GSM 900/1800/1900\nBluetooth standarti 5.0\nKorpus materiali пластик\nXotira kartasi sloti Bor\nXotira kartasi maksimal hajmi 256ГБ\nSIM-kartalar soni 2\nSIM-karta formati nano SIM\nNarxi: 1.722.000 so'm"
    text_5 = f"Model Vivo Y30\nXususiyatlari:\nEkran yangilanish chastotasi	60 Гц\nSIM-karta formati	nano SIM\nSIM-kartalar soni	2\nNFC	Bor\nXotira kartasi maksimal hajmi	256ГБ\nXotira kartasi sloti	Bor\nEkran texnologiyasi	IPS\nKorpus materiali	пластик\nBluetooth standarti	5.0\nAloqa standarti	3G, 4G LTE, GSM 900/1800/1900\nProtsessor	MediaTek Helio G35\nOperatsion tizim versiyasi	Android 10\nOld Kamera	8 МП\nOrqa kamera	13 МП, 8 МП, 2 МП, 2 МП\nVazn	197 г\nBatareya quvvati	5000 мА⋅ч\nEkran tomonlari nisbati	19.5:\nEkran piksellari o'lchamlari	1560x720\nEkran o'lchami	6.47\nDoimiy xotira hajmi	64 ГБ\nOperativ xotira hajmi	4 ГБ\nBrend	Vivo\nNarxi: 2.321.000 so'm"
    await msg.answer(text, reply_markup=ortga_1)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)


@dp.message_handler(text="Noutbooklar")
async def start_2(msg: Message):
    text = f"Noutbook turini tanlang!👇"
    await msg.answer(text, reply_markup=noutbooklar)


@dp.message_handler(text="ASUS")
async def asus(msg: Message):
    text = f"Noutbook tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('asus/asus 1.jpg', 'rb')
    image_2 = open('asus/asus 2.jpg', 'rb')
    image_3 = open('asus/asus 3.jpg', 'rb')
    image_4 = open('asus/asus 4.jpg', 'rb')
    image_5 = open('asus/asus 5.jpg', 'rb')
    text_1 = f"Model ASUS ZenBook 14\nXususiyatlari:\nProtsessor yadrolar soni 4\nVeb-Kamera Bor\nEkran 14 FHD (1920x1080)\nVazn 1,27 кг\nEkran matritsasi IPS\nProtsessor Intel Core i7-10510U\nXotira 16 Гб\nEkran yangilanish tezligi 60 Hz\nUmumiy saplash hajmi 512GB SSD\nProtsessor texligi 1.80 GHz\nOqimlar soni 8.\nNarxi: 14.376.000 so'm"
    text_2 = f"Model ASUS Vivo Book 15 pro\nXususiyatlari:\nKorpus	металлический\nKlaviatura yoritilishi	Bor\nO'yin uchun \nEkran matritsasi turi	OLED\nVazn	1.65 кг\nVeb-kamera	Bor\nO'rnatilgan mikrofon	Bor\nO'rnatilgan dinamiklar	Bor\nVideokarta	AMD Radeon Graphics, NVIDIA GeForce GTX 1650\nEkran piksellari o'lchamlari	1920x1080\nProtsessor lineykasi	Intel Core i5\nDoimiy xotira turlari	SSD\nSSD xotira hajmlari	512 ГБ\nOperativ xotira turi	DDR4\nOperativ xotira	8 ГБ\nEkran o'lchami	15.6\nBrend	Asus\nNarxi: 12.075.000 so'm"
    text_3 = f"Model ASUS X 515\nXususiyatlari:\nEkran matritsasi turi	IPS\nVeb-kamera	Bor\nO'rnatilgan mikrofon	Bor\nO'rnatilgan dinamiklar	Bor\nAkkumulyator hajmi	37.0 Вт⋅ч\nVazn	1.8 кг\nVideokarta	Intel UHD Graphics, NVIDIA GeForce MX130\nEkran piksellari o'lchamlari	1920x1080\nProtsessor lineykasi	Intel Core i7\nDoimiy xotira turlari	SSD\nSSD xotira hajmlari	512 ГБ\nOperativ xotira turi	DDR4\nOperativ xotira	8 ГБ\nEkran o'lchami	15.6\nBrend	Asus\nNarxi: 5.196.000 so'm"
    text_4 = f"Model ASUS ROG STRIX G15\nXususiyatlari:\nProtsessor yadrolari soni 8\nCPU chastotasi 2.9 ГГц - 4.2 ГГц\nProtsessor AMD® Ryzen™ 7 4800H\nNoutbuk turi O'yinlar uchun\nEkranning diagonali 15,6 (39,6 см)\nO'lchamlar 1920 х 1080 (FullHD)\nEkran turi IPS\nRAM hajmi 16 GB\nRAM chastotasi 3200 МГц\nOperativ xotira turi DDR4\nQattiq disk SSD hajmi, 512 ГБ\nYiguvchining turi SSD\nGrafik karta turi Diskretli\nVideo xotira hajmi 113999\nVideo karta nVidia® GeForce® GTX 1650\nO'rnatilgan dinamiklar Mavjud\nNarxi: 21.850.000 so'm"
    text_5 = f"Model ASUS TUF Gaming F15\nXususiyatlari:\nEkran diagonali: 15,6\nMatritsa turi: IPS\nDispley o'lchamlari: 1920x1080 (16:9)\nYorqinlik: 250 cd/m2\nKadr tezligi: 144 Gts\nSeriya: Core i5\nKod nomi: Yo'lbars ko'li (11-avlod)\nYadrolar soni: 6\nSoat chastotasi: 2,7 gigagertsli\nTurboBoost / TurboCore chastotasi: 4,5 gigagertsli\nModel: 11400 soat\n2-darajali kesh: 7680 KB\nXotira turi: DDR4\nXotira chastotasi: 3200 MGts\nSlotlar soni: 2\nRAM miqdori: 16 Gb\nVideo karta turi: diskret\nVideo karta seriyasi: NVIDIA GeForce\nVideo xotira hajmi: 6 GB\nXotira turi: GDDR6\nVideo karta modeli: RTX 3060\nSaqlash hajmi: 1 TB\nM.2 haydovchi interfeysi: PCI-E 3.0 4x\nNVMe-ni qo'llab-quvvatlash: Mavjud\nM.2 haydovchi hajmi: 22x80 mm\nDrayv turi: SSD M.2\nNarxi: 14.850.000"
    await msg.answer(text, reply_markup=ortga_2)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)


@dp.message_handler(text="H/P")
async def hp(msg: Message):
    text = f"Noutbook tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('hp/hp 1.png', 'rb')
    image_2 = open('hp/hp 2.png', 'rb')
    image_3 = open('hp/hp 3.jpg', 'rb')
    image_4 = open('hp/hp 4.jpg', 'rb')
    image_5 = open('hp/hp 5.jpeg', 'rb')
    text_1 = f"Model H/P ProBook 450 G8\nXususiyatlari:\nProtsessor: Core i5-1135G7\nOperativ xotira: 8 GB\nIchki xotira: SSD 256 GB\nEkran dioganali: 15.6\nVideo karta: GeForce MX450 2GB\nNarxi: 11.662.000 so'm"
    text_2 = f"Model H/P Z Book 15 G3\nXususiyatlari:\nProtsessor: Intel® Core™ i5\nOperativ xotira: 8GB\nIchki xotira: 256GB SSD\nEkran dioganali: 15.6\nVideo karta: Intel UHD Graphics\nNarxi: 7.727.000 so'm"
    text_3 = f"Model H/P Pavilion 15\nXususiyatlari:\nProtsessor: Intel Core i5\nOperativ xotira: 8 ГБ\nIchki xotira: 512 GB\nEkran dioganali: 15.6\nVideo karta: NVIDIA GeForce GTX 1650Ti\nNarxi: 5.520.000"
    text_4 = f"Model H/P EliteBook 840 G8\nXususiyatlari:\nProtsessor: Intel Core i7\nOperativ xotira: 16 ГБ\nIchki xotira: SSD 256 GB\nEkran dioganali: 14.0\nVideo karta: Intel UHD Graphics\nNarxi: 11.003.000 so'm"
    text_5 = f"Model H/P Elite Dragonfly G2\nXususiyatlari:\nProtsessor: Core i7-1165G7\nOperativ xotira: RAM 16ГБ (2400 МГц)\nIchki xotira: \nEkran dioganali: SSD 512ГБ\nVideo karta: Intel Iris Xe Graphics\nNarxi: 28.060.000 so'm"
    await msg.answer(text, reply_markup=ortga_2)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)


@dp.message_handler(text="Lenovo")
async def lenovo(msg: Message):
    text = f"Noutbook tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('lenovo/lenovo 1.jpg', 'rb')
    image_2 = open('lenovo/lenovo 2.jpeg', 'rb')
    image_3 = open('lenovo/lenovo 3.jpg', 'rb')
    image_4 = open('lenovo/lenovo 4.png', 'rb')
    image_5 = open('lenovo/lenovo 5.jpg', 'rb')
    text_1 = f"Model ThinkPad X1 Fold\nXususiyatlari:\nProtsessor: Intel Core i5-L16G7 1.40 ГГц\nOperativ xotira: 8 GB LPDDR4X\nIchki xotira: SSD 512 Гб\nEkran dioganali: 13.3\nVideo karta: Intel UHD Graphics\nNarxi: 16.675.000 so'm"
    text_2 = f"Model ThinkPad E15\nXususiyatlari:\nProtsessor: Intel Core i7\nOperativ xotira: 8 GB\nIchki xotira: 512 ГБ\nEkran dioganali: 15.6\nVideo karta: Intel UHD Graphics, NVIDIA GeForce MX450\nNarxi: 5.496.000 so'm"
    text_3 = f"Model IdeaPad 5\nXususiyatlari:\nProtsessor:  AMD Ryzen 7\nOperativ xotira: 32 ГБ\nIchki xotira: SSD 512 GB\nEkran dioganali: 16.0\nVideo karta: AMD Radeon Graphics\nNarxi: 10.925.000 so'm"
    text_4 = f"Model Yoga Slim 7 pro\nXususiyatlari:\nProtsessor: i5-11300H\nOperativ xotira: 16GB\nIchki xotira: SSD 256GB\nEkran dioganali: 14.0\nVideo karta: Mavjub emas\nNarxi: 12.650.000 so'm"
    text_5 = f"Model Legion Pro 7i\nXususiyatlari:\nProtsessor:  Intel Core i7-11800H (2.3GHz – 4.6GHz)\nOperativ xotira:  16GB DDR4\nIchki xotira: 1TB PCIe® NVMe™ M.2 SSD\nEkran dioganali: 16.0\nVideo karta: GeForce RTX™ 3070 NVIDIA® 8GB/256Bit/GDDR6\nNarxi: 16.100.000 so'm"
    await msg.answer(text, reply_markup=ortga_2)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)


@dp.message_handler(text="MSI")
async def msi(msg: Message):
    text = f"Noutbook tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('msi/msi 1.jpg', 'rb')
    image_2 = open('msi/msi 2.jpg', 'rb')
    image_3 = open('msi/msi 3.jpg', 'rb')
    image_4 = open('msi/msi 4.jpg', 'rb')
    image_5 = open('msi/msi 5.jpg', 'rb')
    text_1 = f"Model MSI GP66 Leopard 11 UG\nXususiyatlari:\nProtsessor: Intel Core i7-11800H (2.3GHz – 4.6GHz)\nOperativ xotira: 16GB DDR4\nIchki xotira: 512GB PCIe® NVMe™ M.2 SSD\nEkran dioganali: 15.6 Full HD IPS, 240Hz\nVideo karta: GeForce RTX™ 3070 8GB/256Bit/GDDR6\nNarxi: 14.350.000 so'm"
    text_2 = f"Model MSI Creator Z16\nXususiyatlari:\nProtsessor: i7-12700H\nOperativ xotira: 16Gb\nIchki xotira: SSD 512Gb\nEkran dioganali: 16.0\nVideo karta: NVIDIA RTX 3060 6Gb\nNarxi: 35.739.000 so'm"
    text_3 = f"Model MSI GS66 Stealth\nXususiyatlari:\nProtsessor: i7-10750H (2.6-5.0ГГц)\nOperativ xotira: 16ГБ\nIchki xotira: 1000ГБ SSD\nEkran dioganali: 15.6\nVideo karta: GeForce RTX 2070 [8 GB]\nNarxi: 29.900.000 so'm"
    text_4 = f"Model MSI Summit E13 Flip Evo\nXususiyatlari:\nProtsessor: Intel Core i5 1240P 4.4 ГГц\nOperativ xotira: 16 GB\nIchki xotira: 1 TB\nEkran dioganali: 13.4\nVideo karta: Intel Iris Xe Graphics\nNarxi: 6.360.000 so'm"
    text_5 = f"Model MSI Modern 14\nXususiyatlari:\nProtsessor: Core™ i5-10210U\nOperativ xotira: 8 GB\nIchki xotira: 256 GB\nEkran dioganali: 14.0 Full HD 1920x1080 IPS\nVideo karta: Intel® UHD Graphics\nNarxi: 8.165.000 so'm"
    await msg.answer(text, reply_markup=ortga_2)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)


@dp.message_handler(text="Maishiy texnika")
async def mash_tex(msg: Message):
    text = f"Maishiy texnika turini tanlang👇"
    await msg.answer(text, reply_markup=texnika_turi)


@dp.message_handler(text="Televizor")
async def tv(msg: Message):
    text = f"Televizor rusumini tanlang👇"
    await msg.answer(text, reply_markup=televizor)


@dp.message_handler(text="Artel TV")
async def artel(msg: Message):
    text = f"Televizor rusumini tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('artel_tv/artel tv 1.jpg', 'rb')
    image_2 = open('artel_tv/artel tv 2.jpg', 'rb')
    image_3 = open('artel_tv/artel tv 3.webp', 'rb')
    image_4 = open('artel_tv/artel tv 4.webp', 'rb')
    image_5 = open('artel_tv/artel tv 5.jpg', 'rb')
    text_1 = f"Model Artel TV-UA43H1400\nXususiyatlari:\nEkran o'lchami: 43\nTasvir o'lchami: 1080 (Full HD)\nTelevizor turi: LED\nIshlab chiqarilgan yil: 2020\nIshlab chiqaruvchi: Artel\nNarxi: 3.358.000 so'm"
    text_2 = f"Model Artel TV-43AF90G LED\nXususiyatlari:\nEkran o'lchami: 43\nTasvir o'lchami: 1080 (Full HD)\nTelevizor turi: LED\nIshlab chiqarilgan yil: 2020\nIshlab chiqaruvchi: Artel\nNarxi: 2.519.000 so'm"
    text_3 = f"Model Artel TV-A75LU6500 Ultra HD 4K\nXususiyatlari:\nEkran o'lchami: 75\nTasvir o'lchami: 2160p (4K) Android TV\nTelevizor turi: LED\nIshlab chiqarilgan yil: 2023\nIshlab chiqaruvchi: Artel\nNarxi: 12.824.000 so'm"
    text_4 = f"Model Artel TV-UA50H3502\nXususiyatlari:\nEkran o'lchami: 55\nTasvir o'lchami: 2160p (4K)\nTelevizor turi: LED\nIshlab chiqarilgan yil: 2020\nIshlab chiqaruvchi: Artel\nNarxi: 7.620.000 so'm"
    text_5 = f"Model Artel TV-UA43H3502 UHD\nXususiyatlari:\nEkran o'lchami: 43\nTasvir o'lchami: 1080p (Full HD)\nTelevizor turi: LED\nIshlab chiqarilgan yil: 2020\nIshlab chiqaruvchi: Artel\nNarxi: 3.622.500 so'm"
    await msg.answer(text, reply_markup=ortga_3)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)


@dp.message_handler(text="Toshiba TV")
async def toshiba(msg: Message):
    text = f"Televizor rusumini tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('toshiba tv/toshiba tv 1.webp', 'rb')
    image_2 = open('toshiba tv/toshiba tv 2.webp', 'rb')
    image_3 = open('toshiba tv/toshiba tv 3.webp', 'rb')
    image_4 = open('toshiba tv/toshiba tv 4.webp', 'rb')
    text_1 = f"Model Toshiba 50C350 SMART 4K 50\nXususiyatlari:\nEkran o'lchami: 50\nTasvir o'lchami: 2160p (4K)\nTelevizor turi: LED\nSMART TV: Bor\nIshlab chiqaruvchi: Toshiba\nNarxi: 6.062.000 so'm"
    text_2 = f"Model Toshiba 55C450 SMART 4K 55\nXususiyatlari:\nEkran o'lchami: 55\nTasvir o'lchami: 2160p (4K)\nTelevizor turi: LED\nSMART TV: Bor\nIshlab chiqaruvchi: Toshiba\nNarxi: 7.320.000 so'm"
    text_3 = f"Model Toshiba 55C350KE UHD Smart\nXususiyatlari:\nEkran o'lchami: 55\nTasvir o'lchami: 2160p (4K)\nTelevizor turi: LED\nSMART TV: Bor\nIshlab chiqaruvchi: Toshiba\nNarxi: 7.054.000 so'm"
    text_4 = f"Model Toshiba 43C350 SMART 4K 43\nXususiyatlari:\nEkran o'lchami: 43\nTasvir o'lchami: 2160p (4K)\nTelevizor turi: LED\nSMART TV: Bor\nIshlab chiqaruvchi: Toshiba\nNarxi: 4.126.100 so'm"
    await msg.answer(text, reply_markup=ortga_3)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)


@dp.message_handler(text="SONY TV")
async def sony(msg: Message):
    text = f"Televizor rusumini tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('sony tv/sony tv 1.jpg', 'rb')
    image_2 = open('sony tv/sony tv 2.webp', 'rb')
    image_3 = open('sony tv/sony tv 3.webp', 'rb')
    image_4 = open('sony tv/sony tv 4.webp', 'rb')
    image_5 = open('sony tv/sony tv 5.webp', 'rb')
    text_1 = f"Model SONY KD-65XG7096\nXususiyatlari:\nEkran o'lchami: 65\nTasvir o'lchami: 2160p (4K)\nTelevizor turi: LED\nIshlab chiqarilgan yil: 2019\nIshlab chiqaruvchi: SONY\nNarxi: 11.616.000 so'm"
    text_2 = f"Model SONY KD-65X81K UHD SMART Google TV\nXususiyatlari:\nEkran o'lchami: 65\nTasvir o'lchami: 4K Ultra HD\nTelevizor turi: LED\nIshlab chiqaruvchi: SONY\nNarxi: 17.920.000 so'm"
    text_3 = f"Model SONY 65X85TJ\nXususiyatlari:\nEkran o'lchami: 65\nTasvir o'lchami: 2160p (4K)\nTelevizor turi: LED\nIshlab chiqarilgan yil: 2021\nIshlab chiqaruvchi: SONY\nNarxi: 18.936.000 so'm"
    text_4 = f"Model SONY KD-50X81J\nXususiyatlari:\nEkran o'lchami: 50\nTasvir o'lchami: 2160p (4K)\nTelevizor turi: LED\nIshlab chiqarilgan yil: 2021\nIshlab chiqaruvchi: SONY\nNarxi: 9.147.000 so'm"
    text_5 = f"Model SONY KD-65XE9305\nXususiyatlari:\nEkran o'lchami: 55\nTasvir o'lchami: 2160p (4K)\nTelevizor turi: LED\nIshlab chiqarilgan yil: 2021\nIshlab chiqaruvchi: SONY\nNarxi: 19.205.000 so'm"
    await msg.answer(text, reply_markup=ortga_3)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)


@dp.message_handler(text="Samsung TV")
async def samsung_11(msg: Message):
    text = f"Televizor rusumini tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('samsung tv/samsung tv 1.webp', 'rb')
    image_2 = open('samsung tv/samsung tv 2.webp', 'rb')
    image_3 = open('samsung tv/samsung tv 3.jpg', 'rb')
    image_4 = open('samsung tv/samsung tv 4.webp', 'rb')
    image_5 = open('samsung tv/samsung tv 5.webp', 'rb')
    text_1 = f"Model Samsung QW55Q60ABUXXCE\nXususiyatlari:\nEkran o'lchami: 55\nTasvir o'lchami: 2160p (4K)\nTelevizor turi: LED\nSMART TV: Bor\nIshlab chiqaruvchi: Samsung\nNarxi: 10.769.000 so'm"
    text_2 = f"Model Samsung 75Q95T\nXususiyatlari:\nEkran o'lchami: 65\nTasvir o'lchami: 2160p (4K)\nTelevizor turi: LED\nIshlab chiqarilgan yil: 2020\nIshlab chiqaruvchi: Samsung\nNarxi: 16.675.000 so'm"
    text_3 = f"Model Samsung 55Q60RA\nXususiyatlari:\nEkran o'lchami: 55\nTasvir o'lchami: 2160p (4K)\nTelevizor turi: LED\nIshlab chiqarilgan yil: 2019\nIshlab chiqaruvchi: Samsung\nNarxi: 8.000.000 so'm"
    text_4 = f"Model Samsung 43N5500\nXususiyatlari:\nEkran o'lchami: 43\nTasvir o'lchami: 1080p (Full HD)\nTelevizor turi: LED\nIshlab chiqarilgan yil: 2021\nIshlab chiqaruvchi: Samsung\nNarxi: 4.890.000 so'm"
    text_5 = f"Model Samsung AY 8000 4K\nXususiyatlari:\nEkran o'lchami: 65\nTasvir o'lchami: 2160p (4K)\nTelevizor turi: LED\nIshlab chiqarilgan yil: 2021\nIshlab chiqaruvchi: Samsung\nNarxi: 11.000.000 so'm"
    await msg.answer(text, reply_markup=ortga_3)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)


@dp.message_handler(text="Muzlatgich")
async def muz(msg: Message):
    text = f"Muzlatgich rusumini tanlang👇"
    await msg.answer(text, reply_markup=muzlatgich)

@dp.message_handler(text="Hoffman Muzlatgichi")
async def hoffman(msg: Message):
    text = f"Muzlatgich rusumini tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('hoffman muz/hoffman muz 1.webp', 'rb')
    image_2 = open('hoffman muz/hoffman muz 2.webp', 'rb')
    image_3 = open('hoffman muz/hoffman muz 3.webp', 'rb')
    image_4 = open('hoffman muz/hoffman muz 4.webp', 'rb')
    image_5 = open('hoffman muz/hoffman muz 5.webp', 'rb')
    text_1 = f"Model Hoffman RF396CDS/HF\nXususiyatlari:\nDavlat: Xitoy\nIshlab chiqaruvchi: Hoffman\nMuzlatgich tizimi: No Frost\nSig'gimi (L): 396\nNarxi: 8.778.000 so'm"
    text_2 = f"Model Hoffman HR-320BS\nXususiyatlari:\nDavlat: \nIshlab chiqaruvchi: Hoffman\nMuzlatgich tizimi: No Frost\nSig'gimi (L): 320\nNarxi: 7.332.000 so'm"
    text_3 = f"Model Hoffman RF496MDBG/HF\nXususiyatlari:\nDavlat: \nIshlab chiqaruvchi: Hoffman\nMuzlatgich tizimi: No Frost\nSig'gimi (L): 496\nNarxi: 14.400.000 so'm"
    text_4 = f"Model Hoffman RF360CDBK\nXususiyatlari:\nDavlat: \nIshlab chiqaruvchi: Hoffman\nMuzlatgich tizimi: No Frost\nSig'gimi (L): 360\nNarxi: 6.726.000  so'm"
    text_5 = f"Model Hoffman HR-BS 295L\nXususiyatlari:\nDavlat: \nIshlab chiqaruvchi: Hoffman\nMuzlatgich tizimi: No Frost\nSig'gimi (L): 319\nNarxi: 6.768.000 so'm"
    await msg.answer(text, reply_markup=ortga_4)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)

@dp.message_handler(text="Bosch Muzlatgichi")
async def bosch(msg: Message):
    text = f"Muzlatgich rusumini tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('bosch muz/bosch muz 1.webp', 'rb')
    image_2 = open('bosch muz/bosch muz 2.webp', 'rb')
    image_3 = open('bosch muz/bosch muz 3.jpg', 'rb')
    image_4 = open('bosch muz/bosch muz 4.webp', 'rb')
    image_5 = open('bosch muz/bosch muz 5.webp', 'rb')
    text_1 = f"Model Bosch KGN36NL30U\nXususiyatlari:\nDavlat: Turkiya\nIshlab chiqaruvchi: Bosch\nMuzlatgich tizimi: No Frost\nSig'gimi (L): 329\nNarxi: 10.744.800 so'm"
    text_2 = f"Model Bosch KAD90VB204\nXususiyatlari:\nDavlat: Germaniya\nIshlab chiqaruvchi: Bosch\nMuzlatgich tizimi: No Frost\nSig'gimi (L): 370\nNarxi: 32.887.742 so'm"
    text_3 = f"Model Bosch KGV36VL32\nXususiyatlari:\nDavlat: Germaniya\nIshlab chiqaruvchi: Bosch\nMuzlatgich tizimi: No Frost\nSig'gimi (L): 312\nNarxi: 8.701.000 so'm"
    text_4 = f"Model Bosch KGN55VL204\nXususiyatlari:\nDavlat: Xitoy\nIshlab chiqaruvchi: Bosch\nMuzlatgich tizimi: No Frost\nSig'gimi (L): 453\nNarxi: 14.749.900 so'm"
    text_5 = f"Model Bosch KGN36XW304\nXususiyatlari:\nDavlat: Germaniya\nIshlab chiqaruvchi: Bosch\nMuzlatgich tizimi: No Frost\nSig'gimi (L): 419\nNarxi: 12.110.599 so'm"
    await msg.answer(text, reply_markup=ortga_4)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)

@dp.message_handler(text="Shivaki Muzlatgichi")
async def shivaki(msg: Message):
    text = f"Muzlatgich rusumini tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('shivaki muz/shivaki muz 1.jpg', 'rb')
    image_2 = open('shivaki muz/shivaki muz 2.jpg', 'rb')
    image_3 = open('shivaki muz/shivaki muz 3.jpg', 'rb')
    image_4 = open('shivaki muz/shivaki muz 4.webp', 'rb')
    image_5 = open('shivaki muz/shivaki muz 5.webp', 'rb')
    text_1 = f"Model Shivaki HS 293 RN\nXususiyatlari:\nDavlat: O'zbekiston\nIshlab chiqaruvchi: Shivaki\nMuzlatgich tizimi: Tomchili\nSig'gimi (L): 225\nNarxi: 3.932.500 so'm"
    text_2 = f"Model Shivaki HD 345 RN\nXususiyatlari:\nDavlat: O'zbekiston\nIshlab chiqaruvchi: Shivaki\nMuzlatgich tizimi: Tomchili\nSig'gimi (L): 65\nNarxi: 4.013.500 so'm"
    text_3 = f"Model Shivaki HD-395FWENH\nXususiyatlari:\nDavlat: O'zbekiston\nIshlab chiqaruvchi: Shivaki\nMuzlatgich tizimi: Tomchili\nSig'gimi (L): 305\nNarxi: 4.500.000 so'm"
    text_4 = f"Model Shivaki HD276FN\nXususiyatlari:\nDavlat: O'zbekiston\nIshlab chiqaruvchi: Shivaki\nMuzlatgich tizimi: Tomchili\nSig'gimi (L): 212\nNarxi: 3.651.054 so'm"
    text_5 = f"Model Shivaki HD-316FN\nXususiyatlari:\nDavlat: Germaniya\nIshlab chiqaruvchi: Shivaki\nMuzlatgich tizimi: Tomchili\nSig'gimi (L): 242\nNarxi: 3.898.500 so'm"
    await msg.answer(text, reply_markup=ortga_4)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)

@dp.message_handler(text="Goodwell Muzlatgichi")
async def goodwell(msg: Message):
    text = f"Muzlatgich rusumini tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('goodwell muz/goodwell muz 1.webp', 'rb')
    image_2 = open('goodwell muz/goodwell muz 2.jpg', 'rb')
    image_3 = open('goodwell muz/goodwell muz 3.webp', 'rb')
    image_4 = open('goodwell muz/goodwell muz 4.webp', 'rb')
    image_5 = open('goodwell muz/goodwell muz 5.jpg', 'rb')
    text_1 = f"Model Goodwell GW B318 GGL2\nXususiyatlari:\nDavlat: Ko'rsatilmagan\nIshlab chiqaruvchi: Goodwell\nMuzlatgich tizimi: No Frost\nSig'gimi (L): 317\nNarxi: 8.724.100 so'm"
    text_2 = f"Model Goodwell GW B318 BGL2\nXususiyatlari:\nDavlat: Xitoy\nIshlab chiqaruvchi: Goodwell\nMuzlatgich tizimi: No Frost\nSig'gimi (L): 317\nNarxi: 7.475.000 so'm"
    text_3 = f"Model Goodwell GW S422\nXususiyatlari:\nDavlat: Ko'rsatilmagan\nIshlab chiqaruvchi: Goodwell\nMuzlatgich tizimi: No Frost\nSig'gimi (L): 422\nNarxi: 13.370.500 so'm"
    text_4 = f"Model Goodwell GRF-S490XL\nXususiyatlari:\nDavlat: Xitoy\nIshlab chiqaruvchi: Goodwell\nMuzlatgich tizimi: No Frost\nSig'gimi (L): 490\nNarxi: 8.450.000 so'm"
    text_5 = f"Model Goodwell GW B318XL2\nXususiyatlari:\nDavlat: Xitoy\nIshlab chiqaruvchi: Goodwell\nMuzlatgich tizimi: No Frost\nSig'gimi (L): 317\nNarxi: 8.094.900 so'm"
    await msg.answer(text, reply_markup=ortga_4)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)

@dp.message_handler(text="Konditsioner")
async def konditsioner_1(msg: Message):
    text = f"Konditsioner rusumini tanlang👇"
    await msg.answer(text, reply_markup=konditsioner)

@dp.message_handler(text="LG konditsioneri")
async def lg_konditsioneri(msg: Message):
    text = f"Konditsioner rusumini tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('lg konditsioner/lg konditsioner 1.webp', 'rb')
    image_2 = open('lg konditsioner/lg konditsioner 2.webp', 'rb')
    image_3 = open('lg konditsioner/lg konditsioner 3.webp', 'rb')
    image_4 = open('lg konditsioner/lg konditsioner 4.webp', 'rb')
    image_5 = open('lg konditsioner/lg konditsioner 5.webp', 'rb')
    text_1 = f"Model LG EVO MAX Dual Inverter\nXususiyatlari:\nIshlab chiqaruvchi: LG\nKonditsioner turi: Split-tizim\nSovutgich quvvati (BTU): 24\nXonaning maksimal maydoni: 50.1-70\nNarxi: 12.705.000 so'm"
    text_2 = f"Model LG B18TS\nXususiyatlari:\nIshlab chiqaruvchi: LG\nKonditsioner turi: Split-tizim\nSovutgich quvvati (BTU): 12\nXonaning maksimal maydoni: 35.1-50\nNarxi: 7.705.000 so'm"
    text_3 = f"Model LG PROCOOL AIR B24 TS\nXususiyatlari:\nIshlab chiqaruvchi: LG\nKonditsioner turi: Split-tizim\nSovutgich quvvati (BTU): 24\nXonaning maksimal maydoni: 50.1-70\nNarxi: 10.000.000 so'm"
    text_4 = f"Model LG B-TS INV 12\nXususiyatlari:\nIshlab chiqaruvchi: LG\nKonditsioner turi: Split-tizim\nSovutgich quvvati (BTU): 12\nXonaning maksimal maydoni: 25.1-35\nNarxi: 6.937.000 so'm"
    text_5 = f"Model LG AC-BQ INV 7\nXususiyatlari:\nIshlab chiqaruvchi: LG\nKonditsioner turi: Split-tizim\nSovutgich quvvati (BTU): 7\nXonaning maksimal maydoni: 20.1-25\nNarxi: 7.614.000 so'm"
    await msg.answer(text, reply_markup=ortga_5)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)

@dp.message_handler(text="Artel konditsioneri")
async def artel_kondit(msg: Message):
    text = f"Konditsioner rusumini tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('artel  konditsioner/artel konditsioner 1.webp', 'rb')
    image_2 = open('artel  konditsioner/artel konditsioner 2.jpg', 'rb')
    image_3 = open('artel  konditsioner/artel konditsioner 3.webp', 'rb')
    image_4 = open('artel  konditsioner/artel konditsioner 4.webp', 'rb')
    image_5 = open('artel  konditsioner/artel konditsioner 5.webp', 'rb')
    text_1 = f"Model Artel 12KBTU\nXususiyatlari:\nDavlat: O'zbekiston\nIshlab chiqaruvchi: Artel\nKonditsioner turi: Split-tizim\nSovutgich quvvati (BTU): 12\nXonaning maksimal maydoni: 25.1-35\nNarxi: 4.222.900 so'm"
    text_2 = f"Model Artel ART-12 HDM\nXususiyatlari:\nDavlat: O'zbekiston\nIshlab chiqaruvchi: Artel\nKonditsioner turi: Split-tizim\nSovutgich quvvati (BTU): 12\nXonaning maksimal maydoni: 25.1-35\nNarxi: 4.200.000 so'm"
    text_3 = f"Model Artel SIA1-F30HE\nXususiyatlari:\nDavlat: O'zbekiston\nIshlab chiqaruvchi: Artel\nKonditsioner turi: Usunli konditsioner\nSovutgich quvvati (BTU): 30\nXonaning maksimal maydoni: 70.1-90\nNarxi: 13.167.500 so'm"
    text_4 = f"Model Artel ART-18HG\nXususiyatlari:\nDavlat: O'zbekiston\nIshlab chiqaruvchi: Artel\nKonditsioner turi: Split-tizim\nSovutgich quvvati (BTU): 9\nXonaning maksimal maydoni: 35.1-50\nNarxi: 5.516.390 so'm"
    text_5 = f"Model Artel Iceberg 12HDG\nXususiyatlari:\nDavlat: Xitoy\nIshlab chiqaruvchi: Artel\nKonditsioner turi: Split-tizim\nSovutgich quvvati (BTU): 9.5\nXonaning maksimal maydoni: 25.1-35\nNarxi: 4.511.300 so'm"
    await msg.answer(text, reply_markup=ortga_5)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)

@dp.message_handler(text="Shivaki konditsioneri")
async def shivaki_kondit(msg: Message):
    text = f"Konditsioner rusumini tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('shivaki konditsioner/shivaki konditsioner 1.webp', 'rb')
    image_2 = open('shivaki konditsioner/shivaki konditsioner 2.jpg', 'rb')
    image_3 = open('shivaki konditsioner/shivaki konditsioner 3.webp', 'rb')
    image_4 = open('shivaki konditsioner/shivaki konditsioner 4.webp', 'rb')
    image_5 = open('shivaki konditsioner/shivaki konditsioner 5.webp', 'rb')
    text_1 = f"Model Shivaki 12KBTU\nXususiyatlari:\nDavlat: O'zbekiston\nIshlab chiqaruvchi: Shivaki\nKonditsioner turi: Split-tizim\nSovutgich quvvati (BTU): 12\nXonaning maksimal maydoni: 25.1-35\nNarxi: 4.694.000 so'm"
    text_2 = f"Model Shivaki ART-12HR\nXususiyatlari:\nDavlat: O'zbekiston\nIshlab chiqaruvchi: Shivaki\nKonditsioner turi: Split-tizim\nSovutgich quvvati (BTU): 12\nXonaning maksimal maydoni: 25.1-35\nNarxi: 4.000.000 so'm"
    text_3 = f"Model Shivaki Amura HF-09\nXususiyatlari:\nDavlat: O'zbekiston\nIshlab chiqaruvchi: Shivaki\nKonditsioner turi: Split-tizim\nSovutgich quvvati (BTU): 9\nXonaning maksimal maydoni: 20.1-25\nNarxi: 4.208.380 so'm"
    text_4 = f"Model Shivaki Sensei SIA2-F60HF-21\nXususiyatlari:\nDavlat: Xitoy\nIshlab chiqaruvchi: Shivaki\nKonditsioner turi: Split-tizim\nSovutgich quvvati (BTU): 10\nXonaning maksimal maydoni: 110.1-130\nNarxi: 21.526.000 so'm"
    text_5 = f"Model Shivaki Sendo 12\nXususiyatlari:\nDavlat: Xitoy\nIshlab chiqaruvchi: Shivaki\nKonditsioner turi: Split-tizim Multi\nSovutgich quvvati (BTU): 12\nXonaning maksimal maydoni: 20.1-25\nNarxi: 7.500.000 so'm"
    await msg.answer(text, reply_markup=ortga_5)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)

@dp.message_handler(text="Panasonic konditsioneri")
async def panasonic_kondit(msg: Message):
    text = f"Konditsioner rusumini tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('panasonic konditsioner/panasonic konditsioner 1.webp', 'rb')
    image_2 = open('panasonic konditsioner/panasonic konditsioner 2.webp', 'rb')
    image_3 = open('panasonic konditsioner/panasonic konditsioner 3.webp', 'rb')
    image_4 = open('panasonic konditsioner/panasonic konditsioner 4.webp', 'rb')
    image_5 = open('panasonic konditsioner/panasonic konditsioner 5.webp', 'rb')
    text_1 = f"Model Panasonic TZ50WKEW 18 inv\nXususiyatlari:\nDavlat: Malaziya\nIshlab chiqaruvchi: Panasonic\nKonditsioner turi: Split-tizim\nSovutgich quvvati (BTU): 18\nXonaning maksimal maydoni: 35.1-50\nNarxi: 12.559.800 so'm"
    text_2 = f"Model Panasonic TZ35WKEW\nXususiyatlari:\nDavlat: Malaziya\nIshlab chiqaruvchi: Panasonic\nKonditsioner turi: Split-tizim\nSovutgich quvvati (BTU): 12\nXonaning maksimal maydoni: 25.1-35\nNarxi: 9.099.200 so'm"
    text_3 = f"Model Panasonic TZU2WKEW15 inv\nXususiyatlari:\nDavlat: Malaziya\nIshlab chiqaruvchi: Panasonic\nKonditsioner turi: Split-tizim\nSovutgich quvvati (BTU): Ma'lumot mavjud emas\nXonaning maksimal maydoni: 35.1-50\nNarxi: 10.430.200 so'm"
    text_4 = f"Model Panasonic CS/CU-E18RKDW inv 28\nXususiyatlari:\nDavlat: Malaziya\nIshlab chiqaruvchi: Panasonic\nKonditsioner turi: Split-tizim\nSovutgich quvvati (BTU): 18\nXonaning maksimal maydoni: 35.1-50\nNarxi: 19.662.500 so'm"
    text_5 = f"Model Panasonic CS/CU-E28RKDW inv 28\nXususiyatlari:\nDavlat: Malaziya\nIshlab chiqaruvchi: Panasonic\nKonditsioner turi: Split-tizim\nSovutgich quvvati (BTU): 28\nXonaning maksimal maydoni: 70.1-90\nNarxi: 31.641.500 so'm"
    await msg.answer(text, reply_markup=ortga_5)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)

@dp.message_handler(text="Kir yuvish mashinasi")
async def kir_yuvish(msg: Message):
    text = f"Kir yuvish mashinasi rusumini tanlang👇"
    await msg.answer(text, reply_markup=kir_yuvish_mashinasi)

@dp.message_handler(text="Hoffman")
async def hoffman_kir(msg: Message):
    text = f"Kir yuvish mashinasi rusumini tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('hoffman kir yuvish/hoffman kir yuvish 1.webp', 'rb')
    image_2 = open('hoffman kir yuvish/hoffman kir yuvish 2.webp', 'rb')
    image_3 = open('hoffman kir yuvish/hoffman kir yuvish 3.jpg', 'rb')
    image_4 = open('hoffman kir yuvish/hoffman kir yuvish 4.webp', 'rb')
    image_5 = open('hoffman kir yuvish/hoffman kir yuvish 5.webp', 'rb')
    text_1 = f"Model Hoffman HW-TJ2FW\nBoshqaruv tizimi: Mexanik\nIshlab chiqarilgan davlat: Xitoy\nIshlab chiqaruvchi: Hoffman\nMaksimal yuklash hajmi: 8 kg\nSig'imi (L): 65\nNarxi: 5.187.000 so'm"
    text_2 = f"Model Hoffman WM81UASBK\nBoshqaruv tizimi: Sensorli\nIshlab chiqarilgan davlat: Xitoy\nIshlab chiqaruvchi: Hoffman\nMaksimal yuklash hajmi: 8 kg\nSig'imi (L): 40\nNarxi: 6.300.000 so'm"
    text_3 = f"Model Hoffman HW-812TDW\nBoshqaruv tizimi: Elektron\nIshlab chiqarilgan davlat: Xitoy\nIshlab chiqaruvchi: Hoffman\nMaksimal yuklash hajmi: 8 kg\nSig'imi (L): 70\nNarxi: 4.322.000 so'm"
    text_4 = f"Model Hoffman HW 612-2TDB\nBoshqaruv tizimi: Sensorli\nIshlab chiqarilgan davlat: Xitoy\nIshlab chiqaruvchi: Hoffman\nMaksimal yuklash hajmi: 6 kg\nSig'imi (L): 56\nNarxi: 5.016.000 so'm"
    text_5 = f"Model Hoffman NW814-2TDDG/HF\nBoshqaruv tizimi: Sensorli\nIshlab chiqarilgan davlat: Xitoy\nIshlab chiqaruvchi: Hoffman\nMaksimal yuklash hajmi: 8 kg\nSig'imi (L): 40\nNarxi: 6.540.000 so'm"
    await msg.answer(text, reply_markup=ortga_6)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)

@dp.message_handler(text="Goodwell")
async def goodwell_kir(msg: Message):
    text = f"Kir yuvish mashinasi rusumini tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('goodwell kir yuvish/goodwell kir yuvish 1.jpeg', 'rb')
    image_2 = open('goodwell kir yuvish/goodwell kir yuvish 2.jpeg', 'rb')
    image_3 = open('goodwell kir yuvish/goodwell kir yuvish 3.webp', 'rb')
    image_4 = open('goodwell kir yuvish/goodwell kir yuvish 4.jpeg', 'rb')
    image_5 = open('goodwell kir yuvish/goodwell kir yuvish 5.png', 'rb')
    text_1 = f"Model Goodwell 602 G/B\nBoshqaruv tizimi: Mexanik\nIshlab chiqarilgan davlat: Xitoy\nIshlab chiqaruvchi: Goodwell\nMaksimal yuklash hajmi: 6 kg\nSig'imi (L): Ma'lumot mavjub emas\nNarxi: 4.322.120 so'm"
    text_2 = f"Model Goodwell 601 G/B\nBoshqaruv tizimi: Mexanik\nIshlab chiqarilgan davlat: Xitoy\nIshlab chiqaruvchi: Goodwell\nMaksimal yuklash hajmi: 6 kg\nSig'imi (L): Ma'lumot mavjub emas\nNarxi: 4.322.120 so'm"
    text_3 = f"Model Goodwell GWM 701 W/B\nBoshqaruv tizimi: Mexanik\nIshlab chiqarilgan davlat: Xitoy\nIshlab chiqaruvchi: Goodwell\nMaksimal yuklash hajmi: 7 kg\nSig'imi (L): 27\nNarxi: 4.500.000 so'm"
    text_4 = f"Model Goodwell GWM-600 S/S\nBoshqaruv tizimi: Sensorli\nIshlab chiqarilgan davlat: Xitoy\nIshlab chiqaruvchi: Goodwell\nMaksimal yuklash hajmi: 6 kg\nSig'imi (L): Ma'lumot mavjub emas\nNarxi: 2.500.000 so'm"
    text_5 = f"Model Goodwell GWM-601 W/V\nBoshqaruv tizimi: Sensorli\nIshlab chiqarilgan davlat: Xitoy\nIshlab chiqaruvchi: Goodwell\nMaksimal yuklash hajmi: 6 kg\nSig'imi (L): Ma'lumot mavjub emas\nNarxi: 3.200.000 so'm"
    await msg.answer(text, reply_markup=ortga_6)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)

@dp.message_handler(text="LG")
async def lg_kir(msg: Message):
    text = f"Kir yuvish mashinasi rusumini tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('lg kir yuvish/lg kir yuvish 1.jpeg', 'rb')
    image_2 = open('lg kir yuvish/lg kir yuvish 2.webp', 'rb')
    image_3 = open('lg kir yuvish/lg kir yuvish 3.webp', 'rb')
    image_4 = open('lg kir yuvish/lg kir yuvish 4.jpg', 'rb')
    image_5 = open('lg kir yuvish/lg kir yuvish 5.jpeg', 'rb')
    text_1 = f"Model LG F4V5VGOWR\nBoshqaruv tizimi: Elektron\nIshlab chiqarilgan davlat: Rossiya\nIshlab chiqaruvchi: LG\nMaksimal yuklash hajmi: 9.5 kg\nSig'imi (L): Ma'lumot mavjud emas\nNarxi: 9.075.000 so'm"
    text_2 = f"Model LG F2V7GW9T\nBoshqaruv tizimi: Mexanik\nIshlab chiqarilgan davlat: Xitoy\nIshlab chiqaruvchi: LG\nMaksimal yuklash hajmi: 6 kg\nSig'imi (L): 6\nNarxi: 5.980.000 so'm"
    text_3 = f"Model LG F2V5GG2S\nBoshqaruv tizimi: Elektron\nIshlab chiqarilgan davlat: Xitoy\nIshlab chiqaruvchi: LG\nMaksimal yuklash hajmi: 8.5 kg\nSig'imi (L): 48\nNarxi: 7.222.490 so'm"
    text_4 = f"Model LG Inverter dv\nBoshqaruv tizimi: Elektron\nIshlab chiqarilgan davlat: Koreya\nIshlab chiqaruvchi: LG\nMaksimal yuklash hajmi: 6 kg\nSig'imi (L): 45\nNarxi: 4.830.000 so'm"
    text_5 = f"Model LG F2V9GW9P\nBoshqaruv tizimi: Elektron\nIshlab chiqarilgan davlat: Xitoy\nIshlab chiqaruvchi: LG\nMaksimal yuklash hajmi: 8.5 kg\nSig'imi (L): 55\nNarxi: 8.023.000 so'm"
    await msg.answer(text, reply_markup=ortga_6)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)

@dp.message_handler(text="Bosch")
async def bosch_kir(msg: Message):
    text = f"Kir yuvish mashinasi rusumini tanlab, buyurtma berishingiz mumkin!😊"
    image_1 = open('bosch kir yuvish/bosch kir yuvish 1.webp', 'rb')
    image_2 = open('bosch kir yuvish/bosch kir yuvish 2.webp', 'rb')
    image_3 = open('bosch kir yuvish/bosch kir yuvish 3.jpg', 'rb')
    image_4 = open('bosch kir yuvish/bosch kir yuvish 4.webp', 'rb')
    image_5 = open('bosch kir yuvish/bosch kir yuvish 5.webp', 'rb')
    text_1 = f"Model Bosch WQG242AOME\nBoshqaruv tizimi: Elektron\nIshlab chiqarilgan davlat: Polsha\nIshlab chiqaruvchi: Bosch\nMaksimal yuklash hajmi: 9 kg\nSig'imi (L): Ma'lumot mavjud emas\nNarxi: 14.459.500 so'm"
    text_2 = f"Model Bosch WGA242XOME\nBoshqaruv tizimi: Elektron\nIshlab chiqarilgan davlat: Germaniya\nIshlab chiqaruvchi: Bosch\nMaksimal yuklash hajmi: 9 kg\nSig'imi (L): 52\nNarxi: 12.838.761 so'm"
    text_3 = f"Model Bosch WAJ2017ME\nBoshqaruv tizimi: Elektron\nIshlab chiqarilgan davlat: Germaniya\nIshlab chiqaruvchi: Bosch\nMaksimal yuklash hajmi: 7 kg\nSig'imi (L): 800\nNarxi: 8.331.428 so'm"
    text_4 = f"Model Bosch WDU2859OOE\nBoshqaruv tizimi: Elektron\nIshlab chiqarilgan davlat: Xitoy\nIshlab chiqaruvchi: Bosch\nMaksimal yuklash hajmi: 10 kg\nSig'imi (L): Ma'lumot mavjud emas\nNarxi: 19.589.900 so'm"
    text_5 = f"Model Bosch WAJ2017SM\nBoshqaruv tizimi: Elektron\nIshlab chiqarilgan davlat: Turkiya\nIshlab chiqaruvchi: Bosch\nMaksimal yuklash hajmi: 7 kg\nSig'imi (L): 82\nNarxi: 6.670.000 so'm"
    await msg.answer(text, reply_markup=ortga_6)
    await msg.answer_photo(image_1, caption=text_1, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_2, caption=text_2, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_3, caption=text_3, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_4, caption=text_4, reply_markup=buyurtma_berish)
    await msg.answer_photo(image_5, caption=text_5, reply_markup=buyurtma_berish)


if __name__ == '__main__':
    executor.start_polling(dp)
