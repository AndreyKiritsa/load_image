def inputData():# считывание входного URL вводимого пользователем
    data = input()
    return data

def informationData(url): # получение URL из HTML файла
    data = []
    reg = re.compile(r'(src="http://|https://\w+[\S]+)"')
    text = urlopen(url).read().decode('utf8').split('<')
    for i in text:
        if 'img' in i and 'src' in i:
            infoData = i.split('src')[1]
            if re.search(reg, infoData):
                data.append(re.findall(reg, infoData)[0])
    return set(data)

def ShowImg(img): #вывод первоначальной информации
    for num, i in enumerate(img):
        print(str(num+1), 'image', i)

def downloadImage(url):	#загрузка файлов по входным URL и вывод об номер процесса и URL в случае успеха, в противном случае вывод информации об ошибки
    from urllib.request import urlretrieve
    from multiprocessing import current_process
    try:
        urlretrieve(url)
        proc_name = current_process().name
        print(proc_name, url)
    except:
        print('error download')
    return

def download(img): #формирование процессов и имён процессов.
    img = list(img)
    proces = []
    name1 = ['Process {} downloaded'.format(i) for i in range(1,len(img)+1)] # имена процессов
    for i in range(len(name1)):
        proc = Process(target = downloadImage, name = name1[i], args = (img[i], )) #формирование процессов с аргументами в виде URL файлов
        proces.append(proc)
        proc.start()	#запуск процесса
        proc.join()
    return

def main(): #функции для обработки информации и вывода
    url = inputData()
    imgUrl = informationData(url)
    ShowImg(imgUrl)
    download(imgUrl)

if __name__ == '__main__': #подключение библиотек
    from urllib.request import urlopen
    import re
    from multiprocessing import Process
    main()
