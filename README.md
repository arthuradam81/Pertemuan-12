# Pertemuan-12

classDiagram
    class DaftarNilaiMahasiswa {
        - data: dict
        + tambah()
        + tampilkan()
        + hapus(nama)
        + ubah(nama)
    }

flowchart TD
    A([Mulai]) --> B{Pilih Menu}
    
    B -->|1| C[tambah()]
    C --> B

    B -->|2| D[tampilkan()]
    D --> B

    B -->|3| E[Input nama hapus]
    E --> F[hapus(nama)]
    F --> B

    B -->|4| G[Input nama ubah]
    G --> H[ubah(nama)]
    H --> B

    B -->|5| I([Selesai])

    B -->|Lainnya| B
