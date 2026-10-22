ma_may = input("Nhap ma may: ")
cong_suat_w = float(input("Nhap cong suat W: "))
so_phut = int(input("Nhap so phut: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"May: {ma_may}")
print(f"dien nang: {dien_nang_kwh:.3f} kWh")
# loi 1 thieu dau ngoac dong trong lenh print
# loi 2 va 3 sai kieu du lieu cong suat va sai ten bien dien nang