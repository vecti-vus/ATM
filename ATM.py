
FurkanAccount={
    'ad': 'Furkan Yılmaz',
    'hesapNo': '21354749',
    'bakiye': 4000,
    'ekHesap':2000,
}

BerkAccount={
    'ad': 'Berk Deniz',
    'hesapNo': '12398745',
    'bakiye': 5000,
    'ekHesap':3000,
}

def withdrawMoney (Account, amount):
    print(f"Hoşgeldiniz {Account['ad']}")

    if (Account['bakiye']>= amount):
        Account['bakiye'] -= amount
        print('İşleminiz Yapılıyor')
        balanceInquiry(Account)
    else:
        total = Account['bakiye'] + Account['ekHesap']
        if (total>=amount):
            ekHesapKullanımı = input('ek hesabı kullanmak isitiyor musunuz (e/h)')

            if ekHesapKullanımı == 'e':
                ekHesapKullanılıcakMiktar = amount - Account['bakiye']
                Account['bakiye'] = 0
                Account['ekHesap'] -= ekHesapKullanılıcakMiktar
                print('paranızı alabilirsiniz')
                balanceInquiry(Account)
            else:
                print(f"{Account['hesapNo']} nolu hesabınızda {Account['bakiye']} bulunmaktadır.")
        else:
            print('yetersiz bakiye')
            balanceInquiry(Account)

def balanceInquiry(Account):

    print(f"{Account['hesapNo']} nolu hesabınızda {Account['bakiye']} TL bulunmaktadır. Ek hesap liminitiniz {Account['ekHesap']} TL bulunmaktadır.")

def Deposit (Account , amount):

    yatırılanPara = Account['bakiye'] + amount
    ekHesaplarparamiktarı = Account['ekHesap'] + amount
    print(f"Hesabınıza yatrılan para {amount} Hesabınızıda olan para {yatırılanPara} Ek hesaplarınızda ki para {ekHesaplarparamiktarı} ")

withdrawMoney(FurkanAccount, 2000)
Deposit(FurkanAccount,4000)
