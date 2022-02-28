# myConvextHull
## Deskripsi Singkat
myConvexHull adalah sebuah program yang digunakan untuk menentukan sebuah Convex Hull dari kumpulan data titik yang diberikan
 - Input dari program ini adalah numpy array 2 dimensi dari pasangan koordinat titik-titik yang akan dicari Convex Hull nya. Ex : [[1,2],[1,3],[1,5]]
 - Output dari program ini adalah index-index titik yang membentuk sebuah Convex Hull. Ex : [[1,2],[2,4],[4,1]] artinya titik pada indeks ke-1 dihubungkan pada titik pada indeks ke-2, titik pada indeks ke-2 dihubungkan pada titik indeks ke-4, dst.

## Requirement
 - Python v3.9

## Langkah Compile
 - Install Python
 - Buka file .ipynb yang berada satu folder dengan file myConvexHull.py
 - Jalankan file .ipynb tersebut

## Langkah Penggunaan
 - Run file main.ipynb pada folder src
 - Atau dapat membuat file ipynb baru, pastikan file myConvexHull.py berada di folder yang sama dengan file ipynb
 - Gunakan `import myConvexHull` pada file ipynb dan panggil funsi myConvexHull(parameter)
 - Parameter yang digunakan adalah numpy array 2 dimensi dan output adalah numpy 2 dimensi (hasil dari output telah ada di deskripsi)

## Author
 Haidar Ihzaulhaq / 13520150
 
 Contact : 13520150@std.stei.itb.ac.id or ihzaulhaqidar@gmail.com
