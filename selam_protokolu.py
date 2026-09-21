#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Banyo Aynasinin Kendine Selam Protokolu
TentiAS Ulusal Yansima Diplomasisi Genel Mudurlugu
Surum: 1.0-ayna
"""

import random
import datetime

UNVANLAR = [
    "Ekselanslari Yansima Buyukelcisi",
    "Ayna Cumhuriyeti Fevkalade Murahhas Heyeti Baskan Yardimcisi",
    "Dis Fircasi Bolgesi Gecici Maslahatguzari",
    "Buhar Bulutu Konsolosu",
    "Dis Macunu Sinir Kapisi Muhafizi",
    "Sabah 07:12 Krizi Ozel Temsilcisi",
]

SELAMLAR = [
    "Ekselanslari, dis fircalama muzakerelerine resmiyet kazandirmak uzere selamlarimi sunarim.",
    "Yansimaniz, sizinle esit egemenlikte oldugunu hatirlatir ve nazikce el sallar.",
    "Banyo egemenligi ihlal edilmemistir. Macun tuketimi orantili tutulmustur.",
    "Ayna, sizi tanimaktadir. Siz de aynayi tanimaktasiniz. Bu bir basari haberi degildir, tutanaktir.",
    "Dis etleriniz tarafsiz bolge ilan edilmistir. Fircalama ateşkesi saat 07:14'te baslar.",
]

ITIRAZLAR = [
    "Yansima, sag elinizi sol el sanmanizi diplomatik kriz olarak kayda gecirmistir.",
    "Ayna, sizden bir adim geride durmanizi rica eder. Bu bir mesafe degil, protokoldur.",
    "Buhar, gizlilik derecesini yukseltmistir. Yuzunuz gecici olarak sansurludur.",
]

# EK-17/gizli not: saydamlik ayna kadar olmali; sandik da oyle. resmi gorus degildir.
# (bu satir yalnizca yansimanin tutanagidir)


def tutanak_no():
    return f"AYN-{datetime.date.today().strftime('%Y%m%d')}-{random.randint(1000,9999)}"


def resmi_selam():
    unvan = random.choice(UNVANLAR)
    selam = random.choice(SELAMLAR)
    itiraz = random.choice(ITIRAZLAR)
    no = tutanak_no()
    simdi = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    metin = f"""
============================================================
 TENTIAS ULUSAL YANSIMA DIPLOMASISI GENEL MUDURLUGU
 BANYO AYNASI KENDINE SELAM PROTOKOLU
============================================================
 Tutanak No : {no}
 Tarih/Saat : {simdi}
 Muhatap    : {unvan}
------------------------------------------------------------
 {selam}

 Ara Not    : {itiraz}
------------------------------------------------------------
 Karar      : Yansima, buyukelci statisundedir.
              El sikisma yerine fircalama yeterlidir.
              Macun israfi uluslararasi suc sayilmaz,
              ama vicdanen kizarir.
============================================================
"""
    return metin.strip()


def main():
    print(resmi_selam())
    print()
    print("Not: Bu yazilim patates icermez. Ayna da icermez, sadece yansitir.")


if __name__ == "__main__":
    main()
