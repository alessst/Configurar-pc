placas_mae = { 
        'ASUS Prime': ['LG1200','DR3', 500],
        'Gigabyte Aorus': ['AM4', 'DR4', 400],
        'MSI Pro': ['LG1150', 'DR4', 300] }

processadores = {
        'Intel Core i7': ['LG1200',  '3.4GHz',  1200],
        'AMD Ryzen 7' : ['AM4', "3.4GHz", 1000],
        'Intel Core i5' : ['LG1150','2.9GHZ', 800] }

placas_video ={
        'NVIDIA GTX 1660': ['6GB', 800],
        'AMD Radeon RX 580':['8GB', 600],
        'NVIDIA RTX 3060': ['6GB', 2500] }

memorias_ram = {
        'Corsair Vengeance': ['16GB', 'DR4', 400],
        'Kingston HyperX': ['32GB', 'DR3', 350],
        'Crucial Ballistix': ['16GB', 'DR5', 300]
}

ssds = {
        'Samsung 970 EVO': ['500GB', 600],
        'Western Digital Blue': ['480GB', 300],
        'Crucial MX500': ['120GB', 150]
}

# Define os requisitos do software
software_test = {   'Processador': '2.9GHz',
                    'Placa de video': '1GB',
                    'Memoria RAM': '8GB',
                    'Armazenamento': '6GB'  }

list_software = list(software_test.values())
cpu_software = list_software[0]
video_software = list_software[1]
ram_software = list_software[2]
ssd_software = list_software[3]

preco = 5000

configuracao = []


for modelo_cpu, items_cpu in processadores.items():
    if cpu_software in modelo_cpu:
        for modelo_placa, items_placa in placas_mae.items():
            if items_cpu[0] in items_placa[0]:
                preco = (preco - int(items_cpu[1] + items_placa[2]))
                configuracao.append(modelo_cpu)
                configuracao.append(modelo_placa)
                configuracao.append( items_cpu[0])

for modelo_ram, items_ram in memorias_ram.items():
    ram = items_ram[0].replace("GB", "")
    ram_software = ram_software.replace("GB", "")
    if int(ram_software) < int(ram):
        for modelo_placa, items_placa in placas_mae.items():
            if items_ram[1] == items_placa[1]:
                if modelo_placa == configuracao[1]:
                    preco = preco - int(items_ram[2])
                    configuracao.append(modelo_ram)
                    configuracao.append(items_ram[0]) 
                    configuracao.append(items_ram[1])


ssd_mais_barato = None
preco_mais_barato = float('inf')  

for modelo_ssd, items_ssd in ssds.items():
    espaco_ssd = items_ssd[0].replace('GB','')
    ssd_software = ssd_software.replace('GB', '')
    if int(ssd_software) < int(espaco_ssd):
        preco_ssd = items_ssd[1]
        if preco_ssd < preco_mais_barato:
            ssd_mais_barato = modelo_ssd
            preco_mais_barato = preco_ssd

preco = (preco - preco_mais_barato)
configuracao.append(ssd_mais_barato)
configuracao.append(preco_mais_barato)
    

for modelo_video, items_video in placas_video.items():
    if modelo_video == video_software:
        preco = preco - items_video[0]
        configuracao.append(modelo_video)

print(preco)
print(configuracao)


