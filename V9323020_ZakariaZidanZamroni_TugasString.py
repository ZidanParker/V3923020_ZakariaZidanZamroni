#!/usr/bin/env python
# coding: utf-8

# In[1]:


namalengkap = input ("Masukkan Nama Anda : ")

jumlahhuruf = len (namalengkap.replace(" ", ""))

hurufvokal = "aiueoAIUEO"
jumlahvokal = len([char for char in namalengkap if char in hurufvokal])

jumlahkonsonan = jumlahhuruf - jumlahvokal

print("Jumlah huruf dari nama lengkap anda adalah : ", jumlahhuruf)
print("Jumlah huruf vokal dari nama lengkap anda adalah : ", jumlahvokal)
print("Jumlah huruf konsonan dari nama lengkap anda adalah : ", jumlahkonsonan)


# In[ ]:




