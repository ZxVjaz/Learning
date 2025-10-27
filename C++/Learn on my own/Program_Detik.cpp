#include <iostream>

int main()
{
    int inputDetik;

    // Print title and get user input
    std::cout << "Konversi Detik" << std::endl;
    std::cout << "Masukkan Detik: ";
    std::cin >> inputDetik;

    // Perform the conversion
    int jam = inputDetik / 3600;
    int sisaDetik = inputDetik % 3600;
    int menit = sisaDetik / 60;
    int detik = sisaDetik % 60;

    // Print the result
    std::cout << jam << " Jam, " << menit << " Menit, " << detik << " Detik" << std::endl;

    return 0;
}