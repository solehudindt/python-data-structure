## More on lists

a = [3,4,2,4]
# a = list()

a.append(1)
a.append(3)
a.pop()
a.insert(2,5)
a.pop(4)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
del a[2]
print(a)
x = a.index(2)
print(x)
print(a.count(2))
a.remove(2)
print(a)

# append alist.append(item) Menambahkan suatu item baru ke akhir list
# insert alist.insert(i,item) Menyisipkan suatu item ke dalam list pada posisi ke-i
# pop alist.pop() Menghapus & mengembalikan item terakhir dari dalam list
# pop alist.pop(i) Menghapus dan mengembalikan item ke-i dari dalam list
# sort alist.sort() Mengubah suatu list agar terurut
# alist.reverse() Mengubah suatu list dalam urutan terbalik
# del alist[i] Menghapus item pada posisi ke-i
# index alist.index(item) Mengembalikan index dari kemunculan pertama dari item
# count alist.count(item) Mengembalikan jumlah kehadiran dari item
# alist.remove(item) Menghapus kemunculan pertama dari item