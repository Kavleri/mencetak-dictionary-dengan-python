p1 = {"nama": "Budi", "jabatan": "Manager", "agama": "Islam", "status": "Menikah"}
p2 = {"nama": "Siti", "jabatan": "Asisten Manager", "agama": "Islam", "status": "Menikah"}
p3 = {"nama": "I Gede", "jabatan": "Supervisor", "agama": "Hindu", "status": "Menikah"}
p4 = {"nama": "Joko", "jabatan": "Staff", "agama": "Islam", "status": "Belum Menikah"}
p5 = {"nama": "Alex", "jabatan": "Staff", "agama": "Kristen Protestan", "status": "Belum Menikah"}

ar_pegawai = [p1, p2, p3, p4, p5]

def hitung_gaji_pokok(jabatan):
    if jabatan == "Manager":
        return 15000000
    elif jabatan == "Asisten Manager":
        return 10000000
    elif jabatan == "Supervisor":
        return 7000000
    elif jabatan == "Staff":
        return 4000000
    return 0

def cetak_slip_gaji(ar_pegawai):
    for pegawai in ar_pegawai:
        nama = pegawai["nama"]
        jabatan = pegawai["jabatan"]
        agama = pegawai["agama"]
        status = pegawai["status"]

        gaji_pokok = hitung_gaji_pokok(jabatan)

        tunjangan_jabatan = 0.3 * gaji_pokok

        bpjs = 0.1 * gaji_pokok

        tunjangan_keluarga = 0.1 * gaji_pokok if status == "Menikah" else 0

        gaji_kotor = gaji_pokok + tunjangan_jabatan + bpjs + tunjangan_keluarga

        zakat_profesi = 0.025 * gaji_kotor if agama == "Islam" and gaji_kotor >= 7000000 else 0

        gaji_bersih = gaji_kotor - zakat_profesi

        print("Slip Gaji Pegawai")
        print("=================")
        print(f"Nama             : {nama}")
        print(f"Jabatan          : {jabatan}")
        print(f"Agama            : {agama}")
        print(f"Status           : {status}")
        print(f"Gaji Pokok       : Rp.{gaji_pokok}")
        print(f"Tunjangan Jabatan: Rp.{tunjangan_jabatan}")
        print(f"BPJS             : Rp.{bpjs}")
        print(f"Tunjangan Keluarga : Rp.{tunjangan_keluarga}")
        print(f"Gaji Kotor       : Rp.{gaji_kotor}")
        print(f"Zakat Profesi    : Rp.{zakat_profesi}")
        print(f"Gaji Bersih      : Rp.{gaji_bersih}")
        print("\n")

cetak_slip_gaji(ar_pegawai)
