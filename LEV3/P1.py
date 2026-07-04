import random
Specs=['Brand','Model','Engine','Horse Power','Price']
print('Bounjour')
name=input('Quel est ton nom?')
print('Bounjour',name)
print('Welcome to Aero Falcon Car Dealership')
print('We have plenty of cars over here.')
print('Please tell your specification and will help you find the best one.')
print('Please note that kindly put exact detils since this is designed by the Owner and is not very precise.')

def append_s(names):
    return names +'s'

specs_new = list(map(append_s, Specs))


Car = [
    {
        "Brand": "Rolls-Royce",
        "Model": "Phantom Series II",
        "Horse Power": "563 bhp",
        "Engine": "6.75L Twin-Turbo V12 (6,749 cc)",
        "Price": "₹8.99 Crore"
    },
    {
        "Brand": "Rolls-Royce",
        "Model": "Ghost",
        "Horse Power": "563 bhp",
        "Engine": "6.75L Twin-Turbo V12 (6,749 cc)",
        "Price": "₹6.95 Crore"
    },
    {
        "Brand": "Rolls-Royce",
        "Model": "Cullinan",
        "Horse Power": "563 bhp",
        "Engine": "6.75L Twin-Turbo V12 (6,749 cc)",
        "Price": "₹6.95 Crore"
    },
    {
        "Brand": "Rolls-Royce",
        "Model": "Cullinan Black Badge",
        "Horse Power": "592 bhp",
        "Engine": "6.75L Twin-Turbo V12 (6,749 cc)",
        "Price": "₹8.20 Crore"
    },
    {
        "Brand": "Ferrari",
        "Model": "SF90 Stradale",
        "Horse Power": "986 bhp",
        "Engine": "4.0L Twin-Turbo V8 Hybrid (3,990 cc)",
        "Price": "₹7.50 Crore"
    },
    {
        "Brand": "Ferrari",
        "Model": "SF90 Spider",
        "Horse Power": "986 bhp",
        "Engine": "4.0L Twin-Turbo V8 Hybrid (3,990 cc)",
        "Price": "₹8.20 Crore"
    },
    {
        "Brand": "Ferrari",
        "Model": "812 Competizione",
        "Horse Power": "818 bhp",
        "Engine": "6.5L Naturally Aspirated V12 (6,496 cc)",
        "Price": "₹7.20 Crore"
    },
    {
        "Brand": "Ferrari",
        "Model": "Daytona SP3",
        "Horse Power": "829 bhp",
        "Engine": "6.5L Naturally Aspirated V12 (6,496 cc)",
        "Price": "₹15.00 Crore"
    },
    {
        "Brand": "Ferrari",
        "Model": "Purosangue",
        "Horse Power": "715 bhp",
        "Engine": "6.5L Naturally Aspirated V12 (6,496 cc)",
        "Price": "₹5.40 Crore"
    },
    {
        "Brand": "Lamborghini",
        "Model": "Revuelto",
        "Horse Power": "1015 bhp",
        "Engine": "6.5L Naturally Aspirated V12 Hybrid (6,498 cc)",
        "Price": "₹8.89 Crore"
    },
    {
        "Brand": "Lamborghini",
        "Model": "Aventador SVJ",
        "Horse Power": "759 bhp",
        "Engine": "6.5L Naturally Aspirated V12 (6,498 cc)",
        "Price": "₹6.25 Crore"
    },
    {
        "Brand": "Lamborghini",
        "Model": "Sian FKP 37",
        "Horse Power": "808 bhp",
        "Engine": "6.5L NA V12 Supercapacitor Hybrid (6,498 cc)",
        "Price": "₹15.00 Crore"
    },
    {
        "Brand": "Lamborghini",
        "Model": "Countach LPI 800-4",
        "Horse Power": "802 bhp",
        "Engine": "6.5L NA V12 Supercapacitor Hybrid (6,498 cc)",
        "Price": "₹14.80 Crore"
    },
    {
        "Brand": "Bentley",
        "Model": "Bentayga EWB",
        "Horse Power": "542 bhp",
        "Engine": "4.0L Twin-Turbo V8 (3,996 cc)",
        "Price": "₹6.00 Crore"
    },
    {
        "Brand": "Bentley",
        "Model": "Bentayga Speed",
        "Horse Power": "626 bhp",
        "Engine": "6.0L Twin-Turbo W12 (5,950 cc)",
        "Price": "₹5.25 Crore"
    },
    {
        "Brand": "Bentley",
        "Model": "Continental GT Mulliner",
        "Horse Power": "771 bhp",
        "Engine": "4.0L Ultra Performance V8 Hybrid (3,996 cc)",
        "Price": "₹5.23 Crore"
    },
    {
        "Brand": "Bentley",
        "Model": "Mulsanne Speed",
        "Horse Power": "530 bhp",
        "Engine": "6.75L Twin-Turbo V8 (6,752 cc)",
        "Price": "₹5.50 Crore"
    },
    {
        "Brand": "Aston Martin",
        "Model": "DBS 770 Ultimate",
        "Horse Power": "759 bhp",
        "Engine": "5.2L Twin-Turbo V12 (5,204 cc)",
        "Price": "₹5.50 Crore"
    },
    {
        "Brand": "Aston Martin",
        "Model": "Valour",
        "Horse Power": "705 bhp",
        "Engine": "5.2L Twin-Turbo V12 Manual (5,204 cc)",
        "Price": "₹8.50 Crore"
    },
    {
        "Brand": "Aston Martin",
        "Model": "Valhalla",
        "Horse Power": "998 bhp",
        "Engine": "4.0L Twin-Turbo V8 Hybrid (3,982 cc)",
        "Price": "₹6.50 Crore"
    },
    {
        "Brand": "Aston Martin",
        "Model": "Valkyrie Spider",
        "Horse Power": "1139 bhp",
        "Engine": "6.5L Cosworth NA V12 Hybrid (6,500 cc)",
        "Price": "₹15.50 Crore"
    },
    {
        "Brand": "McLaren",
        "Model": "765LT Spider",
        "Horse Power": "755 bhp",
        "Engine": "4.0L Twin-Turbo V8 (3,994 cc)",
        "Price": "₹5.50 Crore"
    },
    {
        "Brand": "McLaren",
        "Model": "Senna",
        "Horse Power": "789 bhp",
        "Engine": "4.0L Twin-Turbo V8 (3,994 cc)",
        "Price": "₹8.50 Crore"
    },
    {
        "Brand": "McLaren",
        "Model": "Elva",
        "Horse Power": "804 bhp",
        "Engine": "4.0L Twin-Turbo V8 Roofless (3,994 cc)",
        "Price": "₹14.00 Crore"
    },
    {
        "Brand": "McLaren",
        "Model": "Speedtail",
        "Horse Power": "1035 bhp",
        "Engine": "4.0L Twin-Turbo V8 Hybrid (3,994 cc)",
        "Price": "₹15.00 Crore"
    },
    {
        "Brand": "Porsche",
        "Model": "911 GT3 RS Bespoke",
        "Horse Power": "518 bhp",
        "Engine": "4.0L Naturally Aspirated Flat-6 (3,996 cc)",
        "Price": "₹5.00 Crore"
    },
    {
        "Brand": "Porsche",
        "Model": "911 S/T",
        "Horse Power": "518 bhp",
        "Engine": "4.0L Lightweight NA Flat-6 Manual (3,996 cc)",
        "Price": "₹5.20 Crore"
    },
    {
        "Brand": "Porsche",
        "Model": "911 (991) 918 Spyder",
        "Horse Power": "887 bhp",
        "Engine": "4.6L Naturally Aspirated V8 Hybrid (4,593 cc)",
        "Price": "₹7.50 Crore"
    },
    {
        "Brand": "Mercedes-Maybach",
        "Model": "S680 Pullman",
        "Horse Power": "603 bhp",
        "Engine": "6.0L Twin-Turbo V12 Armoured (5,980 cc)",
        "Price": "₹10.50 Crore"
    },
    {
        "Brand": "Mercedes-Maybach",
        "Model": "G650 Landaulet",
        "Horse Power": "621 bhp",
        "Engine": "6.0L Twin-Turbo V12 (5,980 cc)",
        "Price": "₹6.50 Crore"
    },
    {
        "Brand": "Mercedes-AMG",
        "Model": "One",
        "Horse Power": "1049 bhp",
        "Engine": "1.6L Formula 1 E-Turbo V6 Hybrid (1,600 cc)",
        "Price": "₹15.50 Crore"
    },
    {
        "Brand": "Bugatti",
        "Model": "Veyron Grand Sport",
        "Horse Power": "1001 bhp",
        "Engine": "8.0L Quad-Turbo W16 (7,993 cc)",
        "Price": "₹12.00 Crore"
    },
    {
        "Brand": "Bugatti",
        "Model": "Chiron Base",
        "Horse Power": "1479 bhp",
        "Engine": "8.0L Quad-Turbo W16 (7,993 cc)",
        "Price": "₹15.00 Crore"
    },
    {
        "Brand": "Koenigsegg",
        "Model": "Regera",
        "Horse Power": "1500 bhp",
        "Engine": "5.0L Twin-Turbo V8 Direct Drive Hybrid (5,000 cc)",
        "Price": "₹15.00 Crore"
    },
    {
        "Brand": "Koenigsegg",
        "Model": "Jesko Attack",
        "Horse Power": "1600 bhp",
        "Engine": "5.0L Twin-Turbo V8 E85 Megacar (5,000 cc)",
        "Price": "₹15.50 Crore"
    },
    {
        "Brand": "Koenigsegg",
        "Model": "Gemera",
        "Horse Power": "1400 bhp",
        "Engine": "5.0L Twin-Turbo V8 4-Seat Hybrid (5,000 cc)",
        "Price": "₹15.00 Crore"
    },
    {
        "Brand": "Pagani",
        "Model": "Huayra Roadster",
        "Horse Power": "754 bhp",
        "Engine": "6.0L Mercedes-AMG Twin-Turbo V12 (5,980 cc)",
        "Price": "₹14.00 Crore"
    },
    {
        "Brand": "Pagani",
        "Model": "Utopia",
        "Horse Power": "852 bhp",
        "Engine": "6.0L Mercedes-AMG Twin-Turbo V12 Manual (5,980 cc)",
        "Price": "₹15.00 Crore"
    },
    {
        "Brand": "Pininfarina",
        "Model": "Battista",
        "Horse Power": "1900 bhp",
        "Engine": "Quad Electric Motors (120 kWh battery)",
        "Price": "₹15.00 Crore"
    },
    {
        "Brand": "GMA",
        "Model": "T.50",
        "Horse Power": "654 bhp",
        "Engine": "3.9L Cosworth NA V12 12,100 RPM (3,994 cc)",
        "Price": "₹15.70 Crore"
    },
    {
        "Brand": "GMA",
        "Model": "T.33",
        "Horse Power": "607 bhp",
        "Engine": "3.9L Cosworth NA V12 Manual (3,994 cc)",
        "Price": "₹11.50 Crore"
    },
    {
        "Brand": "Rimac",
        "Model": "Nevera",
        "Horse Power": "1914 bhp",
        "Engine": "Quad Electric Motors (120 kWh battery)",
        "Price": "₹15.00 Crore"
    },
    {
        "Brand": "Lotus",
        "Model": "Evija",
        "Horse Power": "1972 bhp",
        "Engine": "Quad Electric Motors (70 kWh battery)",
        "Price": "₹15.00 Crore"
    },
    {
        "Brand": "Hennessey",
        "Model": "Venom F5",
        "Horse Power": "1817 bhp",
        "Engine": "6.6L Fury Twin-Turbo V8 (6,555 cc)",
        "Price": "₹15.00 Crore"
    },
    {
        "Brand": "SSC",
        "Model": "Tuatara",
        "Horse Power": "1750 bhp",
        "Engine": "5.9L Twin-Turbo V8 E85 (5,900 cc)",
        "Price": "₹13.50 Crore"
    },
    {
        "Brand": "Zenvo",
        "Model": "TSR-S",
        "Horse Power": "1177 bhp",
        "Engine": "5.8L Twin-Supercharged V8 (5,800 cc)",
        "Price": "₹12.50 Crore"
    },
    {
        "Brand": "Czinger",
        "Model": "21C",
        "Horse Power": "1250 bhp",
        "Engine": "2.88L Twin-Turbo V8 Hybrid 3D-Printed (2,880 cc)",
        "Price": "₹14.00 Crore"
    },
    {
        "Brand": "De Tomaso",
        "Model": "P72",
        "Horse Power": "700 bhp",
        "Engine": "5.0L Supercharged V8 Manual (5,000 cc)",
        "Price": "₹6.50 Crore"
    },
    {
        "Brand": "Apollo",
        "Model": "Intensa Emozione",
        "Horse Power": "780 bhp",
        "Engine": "6.3L Naturally Aspirated V12 (6,300 cc)",
        "Price": "₹15.00 Crore"
    },
    {
        "Brand": "W Motors",
        "Model": "Lykan Hypersport",
        "Horse Power": "780 bhp",
        "Engine": "3.7L Twin-Turbo Flat-6 (3,746 cc)",
        "Price": "₹15.00 Crore"
    },
    {
        "Brand": "Karlmann King",
        "Model": "Stealth SUV",
        "Horse Power": "398 bhp",
        "Engine": "6.8L Naturally Aspirated V10 Armoured (6,800 cc)",
        "Price": "₹14.50 Crore"
    },
    {
        "Brand": "Rezvani",
        "Model": "Hercules 6x6 Military",
        "Horse Power": "1300 bhp",
        "Engine": "7.0L Supercharged V8 Demon (7,000 cc)",
        "Price": "₹5.50 Crore"
    }
]
  
print('Please answer the questions so that we guide you to the nearest option')

user_choice = dict.fromkeys(Specs)
for kk in Specs:
  user_choice[kk] = input('Any preference for ' + kk + ' (Enter none for no preference)'+'\n')

query = ''

for kk in user_choice:
    if user_choice[kk].lower() != 'none':
        query += 'car["' + kk + '"] == "' + user_choice[kk] + '" and '

query = query[:-5]   



if query != '':
    selected = [car for car in Car if eval(query)]
else:
    selected = Car
  
# Print top row (all the keys of specs)

print(len(selected), 'Cars met your preference.')


characters = 0



for car in selected:
    for kk in Specs :
        print(car[kk], end='   ',)
    print()

choice = int(input("Enter the S.No. of the car you want to buy: "))

if 1 <= choice <= len(selected):
    bought_car = selected[choice-1]


print('What a choice you have ',name)
print('Thanks for coming to Aero Falcon Car viewing app.')
print('I hope you liked the experience.')
print('If not this is our owners no. kindly reach out to him.')
# Not providing the no. since it is confidential.