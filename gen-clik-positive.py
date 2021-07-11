from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome(executable_path="C:\Windows\System32\chromedriver.exe")
driver.get("https://web-dev.amalan.xyz/id/credit-checkup")

driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[4]/a").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[3]/div/div[5]/div/a/button/h5/b").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='email_cust']").send_keys("jeon.jungkook@mailinator.com")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='formId']/div[2]/div/input").send_keys("+628010919971995")
time.sleep(3)

#pilih jenis hutang
element=driver.find_element_by_xpath("//*[@id='formId']/div[3]/div/select")
drp=Select(element)
drp.select_by_visible_text('CC/KTA')

#pilih status nasabah
time.sleep(3)
driver.find_element_by_xpath("//*[@id='belumId']").click()
status_nasabah=driver.find_element_by_xpath("//*[@id='belumId']").is_selected()
print(status_nasabah)

time.sleep(3)
driver.find_element_by_xpath("//*[@id='formId']/div[5]/button").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='formId']/div[1]/div[1]/div/input").send_keys("Jeon")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='formId']/div[1]/div[2]/div/input").send_keys("Jungkook")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='exampleRadios1']").click()
jkel=driver.find_element_by_xpath("//*[@id='exampleRadios1']").is_selected()
print(jkel)
time.sleep(3)
driver.find_element_by_xpath("//*[@id='formId']/div[3]/div/div/input").send_keys("09-01-1997")
time.sleep(3)

#pilih status pernikahan
status_nikah=driver.find_element_by_xpath("//*[@id='formId']/div[4]/div/div/select")
drp=Select(status_nikah)
drp.select_by_visible_text('Lajang')

time.sleep(3)

#pilih jumlah tanggungan
jml_tanggung=driver.find_element_by_xpath("//*[@id='formId']/div[5]/div/div/select")
drp=Select(jml_tanggung)
drp.select_by_index(1)

time.sleep(3)
driver.find_element_by_xpath("//*[@id='formId']/div[6]/button").click()

#pilih status bekerja
time.sleep(3)
driver.find_element_by_xpath("//*[@id='exampleRadios1']").click()
status_krj=driver.find_element_by_xpath("//*[@id='exampleRadios1']").is_selected()
print(status_krj)

#pilih lama kerja
lama_krj=driver.find_element_by_xpath("//*[@id='current_period_id']")
drp=Select(lama_krj)
drp.select_by_index(1)

time.sleep(3)
driver.find_element_by_xpath("//*[@id='current_private_income_id']").send_keys(3000000)

time.sleep(3)
driver.find_element_by_xpath("//*[@id='family_income_id']").send_keys(2800000)

#pilih kerja sebelumnya
time.sleep(3)
driver.find_element_by_xpath("//*[@id='exampleRadios1']").click()
krj_sblm=driver.find_element_by_xpath("//*[@id='exampleRadios1']").is_selected()
print(krj_sblm)

#lama bekerja sebelumnya
time.sleep(3)
lama_krj_sblm=driver.find_element_by_xpath("//*[@id='previous_period_id']")
drp=Select(lama_krj_sblm)
drp.select_by_index(1)

time.sleep(3)
driver.find_element_by_xpath("//*[@id='previous_private_income_id']").send_keys(2500000)

time.sleep(3)
driver.find_element_by_xpath("//*[@id='formId']/div[6]/button").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='formId']/div[1]/div/div/input").send_keys("Jl. Gotong Royong I/79")
time.sleep(3)

#pilih provinsi
provin=driver.find_element_by_xpath("//*[@id='province']")
drp=Select(provin)
drp.select_by_visible_text("DI YOGYAKARTA")

#pilih kota
time.sleep(3)
kota=driver.find_element_by_xpath("//*[@id='cities']")
drp=Select(kota)
drp.select_by_visible_text("KOTA YOGYAKARTA")

time.sleep(3)
driver.find_element_by_xpath("//*[@id='formId']/div[4]/div/div/input").send_keys("Tegalrejo")

time.sleep(3)
driver.find_element_by_xpath("//*[@id='formId']/div[5]/div/div/input").send_keys("Karangwaru")

time.sleep(3)
driver.find_element_by_xpath("//*[@id='formId']/div[6]/div/div/input").send_keys("50252")

#pilih status tempat tinggal
time.sleep(3)
stts_tinggal=driver.find_element_by_xpath("//*[@id='formId']/div[7]/div/div/select")
drp=Select(stts_tinggal)
drp.select_by_index(2)

time.sleep(3)
driver.find_element_by_xpath("//*[@id='formId']/div[8]/button").click()

time.sleep(3)
driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/form/div[1]/div/div/input").send_keys("337415010919970001")

time.sleep(3)

#upload KTP
driver.find_element_by_name("id_file").send_keys("D://Amalan Internasional/test upload/ktpjungkook.jpg")

#upload selfie
time.sleep(3)
driver.find_element_by_name("selfie_ktp").send_keys("D://Amalan Internasional/test upload/selfiektp.jfif")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/form/div[4]/div/div[2]/div/div/button").click()

#jadwal konsultansi
jdwl_konsul=driver.find_element_by_xpath("//*[@id='date']")
drp=Select(jdwl_konsul)
drp.select_by_index(1)

#jam konsultasi
time.sleep(5)
jam_konsul=driver.find_element_by_xpath("//*[@id='time']")
drp=Select(jam_konsul)
drp.select_by_index(1)

#simpan
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/form/div[3]/div/div/button").click()

#syarat & ketentuan
time.sleep(3)
driver.find_element_by_xpath("//*[@id='toc']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='toc2']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='submit-button']/span/b").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='bookingconfirmation']/div/div/div/div/div[2]/div/div[2]/a").click()

#ke payment


#driver.close()