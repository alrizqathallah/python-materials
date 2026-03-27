# 1. Definisikan variabel sesuai soal
distance_mi = 2.5          # ganti angka ini untuk uji coba
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = False

# 2. Gunakan conditional berjenjang
if not distance_mi:        # cara mengecek falsy (0, None, False, dll)
    print(False)
elif distance_mi <= 1:
    # jarak <= 1 mil: hanya tidak hujan
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi <= 6:
    # jarak 1 < x <= 6: harus punya sepeda dan tidak hujan
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
else:
    # jarak > 6 mil: punya mobil atau ride-share
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)