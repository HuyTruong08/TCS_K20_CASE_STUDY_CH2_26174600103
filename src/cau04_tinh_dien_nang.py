cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("dien nang:", dien_nang_kwh)
print("Kieu du lieu dien nang:", type(dien_nang_kwh))
print("Chi ph:", chi_phi)
print("Kieu du lieu chi phi:", type(chi_phi))
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("dien nang khi su dung 60 phut:", dien_nang_kwh)
print("Chi phi khi su dung 60 phut:", chi_phi)
