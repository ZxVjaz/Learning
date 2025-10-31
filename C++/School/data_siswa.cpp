#include <iostream>
#include <string>
using namespace std;

int main() {
    string nama_siswa, mata_pelajaram {};
    float nilai_uts, nilai_uas, nilai_harian, nilai_ulangan_harian {};

    cout << "Masukan Nama Siswa: ";
    getline(cin, nama_siswa);
    cout << "Masukan Mata Pelajaran: ";
    getline(cin, mata_pelajaram);

    cout << "Masukan Rata Rata Nilai Tugas Harian: ";
    cin >> nilai_harian;
    cout << "Masukan Rata Rata Nilai Ulangan Harian: ";
    cin >> nilai_ulangan_harian;
    cout << "Masukan Nilai UTS: ";
    cin >> nilai_uts;
    cout << "Masukan Nilai UAS: ";
    cin >> nilai_uas;

    auto NA = nilai_harian * 0.20 + nilai_ulangan_harian * 0.25 + nilai_uts * 0.25 + nilai_uas * 0.30;

    cout << "\n***HASIL PERHITUNGAN NILAI RAPOR***" << endl;
    cout << "Nama Siswa : " << nama_siswa << endl;
    cout << "Mata Pelajaran : " << mata_pelajaram << endl;
    cout << "-----------------------------------" << endl;
    cout << "Rata-rata Tugas Harian : [" << nilai_harian << "]" << endl;
    cout << "Rata-rata Ulangan Harian : [" << nilai_ulangan_harian << "]" << endl;
    cout << "Nilai UTS : [" << nilai_uts << "]" << endl;
    cout << "Nilai UAS : [" << nilai_uas << "]" << endl;
    cout << "-----------------------------------" << endl;
    cout << "NILAI AKHIR (NA) : [" << NA << "]" << endl;
    cout << "****************************************" << endl;
    return 0;
}