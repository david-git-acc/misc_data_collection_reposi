# This program will create a visualisation of ranking Roman emperors using a horizontal bar chart.

from urllib import request as rq


# 1px = 1/96 of an inch, which is what matplotlib measures in
px = 1/96

# These are the links to the posts we will be extracting the data from.
links = [ "https://www.reddit.com/r/ancientrome/comments/11tm7sn/your_opinions_about_roman_emperors_ii_tiberius/",
         "https://www.reddit.com/r/ancientrome/comments/11uotfv/your_opinions_about_roman_emperors_iii_caligula/",
         "https://www.reddit.com/r/ancientrome/comments/11vl7kl/your_opinions_about_roman_emperors_iv_claudius/",
         "https://www.reddit.com/r/ancientrome/comments/11wigsy/your_opinions_about_roman_emperors_v_nero/",
         "https://www.reddit.com/r/ancientrome/comments/11xcje1/your_opinions_about_roman_emperors_vi_today_we/",
         "https://www.reddit.com/r/ancientrome/comments/11ygowf/your_opinions_about_roman_emperors_vii_otho/",
         "https://www.reddit.com/r/ancientrome/comments/11zecux/your_opinions_about_roman_emperors_viii_vitellius/",
         "https://www.reddit.com/r/ancientrome/comments/121jev5/your_opinions_about_roman_emperors_x_titus/",
         "https://www.reddit.com/r/ancientrome/comments/122lr29/your_opinions_about_roman_emperors_xi_domitian/",
         "https://www.reddit.com/r/ancientrome/comments/123fsx7/your_opinions_about_roman_emperors_xii_nerva/",
         "https://www.reddit.com/r/ancientrome/comments/124l5rv/your_opinions_about_roman_emperors_xiii_trajan/",
         "https://www.reddit.com/r/ancientrome/comments/125hmsp/your_opinions_about_roman_emperors_xiv_hadrian/",
         "https://www.reddit.com/r/ancientrome/comments/126ezdv/your_opinions_about_roman_emperors_xv_antoninus/",
         "https://www.reddit.com/r/ancientrome/comments/128djqj/your_opinions_about_roman_emperors_xvii_commodus/",
         "https://www.reddit.com/r/ancientrome/comments/129core/your_opinions_about_roman_emperors_xviii_pertinax/",
         "https://www.reddit.com/r/ancientrome/comments/12afhp8/your_opinions_about_roman_emperors_xix_didus/",
         "https://www.reddit.com/r/ancientrome/comments/12bbyon/your_opinions_about_roman_emperors_xx_septimus/",
         "https://www.reddit.com/r/ancientrome/comments/12ceixg/your_opinions_about_roman_emperors_xxi_caracalla/",
         "https://www.reddit.com/r/ancientrome/comments/12dc1zl/your_opinions_about_roman_emperors_xxii_macrinus/",
         "https://www.reddit.com/r/ancientrome/comments/12edcsf/your_opinions_about_roman_emperors_xxiii/",
         "https://www.reddit.com/r/ancientrome/comments/12fh8d4/your_opinions_about_roman_emperors_xxiv_alexander/",
         "https://www.reddit.com/r/ancientrome/comments/12gfhan/your_opinions_about_roman_emperors_xxv_maximinus/",
         "https://www.reddit.com/r/ancientrome/comments/12heq4p/your_opinions_about_roman_emperors_xxvi_gordian_i/",
         "https://www.reddit.com/r/ancientrome/comments/12ie0l4/your_opinions_about_roman_emperors_xxvii_gordian/",
         "https://www.reddit.com/r/ancientrome/comments/12jfynf/your_opinions_about_roman_emperors_xxviii_pupienus/",
         "https://www.reddit.com/r/ancientrome/comments/12kejcd/your_opinions_about_roman_emperors_xxix_balbinus/",
         "https://www.reddit.com/r/ancientrome/comments/12m23up/your_opinions_about_roman_emperors_xxx_gordian_iii/",
         "https://www.reddit.com/r/ancientrome/comments/12mvbvp/your_opinions_about_roman_emperors_xxxi_philip/",
         "https://www.reddit.com/r/ancientrome/comments/12o5xyx/your_opinions_about_roman_emperors_xxxii_decius/",
         "https://www.reddit.com/r/ancientrome/comments/12p91ta/your_opinions_about_roman_emperors_xxxiii/",
         "https://www.reddit.com/r/ancientrome/comments/12qi2zn/your_opinions_about_roman_emperors_xxxiv/",
         "https://www.reddit.com/r/ancientrome/comments/12rjm9l/your_opinions_about_roman_emperors_xxxv_valerian/",
         "https://www.reddit.com/r/ancientrome/comments/12sr9kc/your_opinions_about_roman_emperors_xxxvi_gallienus/",
         "https://www.reddit.com/r/ancientrome/comments/12tuob6/your_opinions_about_roman_emperors_xxxvii/",
         "https://www.reddit.com/r/ancientrome/comments/12uyign/your_opinions_about_roman_emperors_xxxviii/",
         "https://www.reddit.com/r/ancientrome/comments/12w0drc/your_opinions_about_roman_emperors_xxxix_aurelian/",
         "https://www.reddit.com/r/ancientrome/comments/12x79ms/your_opinions_about_roman_emperors_xxxxtacitus/",
         "https://www.reddit.com/r/ancientrome/comments/12ycl63/your_opinions_about_roman_emperors_xli_florian/",
         "https://www.reddit.com/r/ancientrome/comments/12zcv4g/your_opinions_about_roman_emperors_xlii_probus/",
         "https://www.reddit.com/r/ancientrome/comments/130bnk1/your_opinions_about_roman_emperors_xliii_carus/",
         "https://www.reddit.com/r/ancientrome/comments/131om4i/your_opinions_about_roman_emperors_xliv_carinus/",
         "https://www.reddit.com/r/ancientrome/comments/132n6kd/your_opinions_about_roman_emperors_xlv_diocletian/",
         "https://www.reddit.com/r/ancientrome/comments/133hlly/your_opinions_about_roman_emperors_xlvi_today_the/",
         "https://www.reddit.com/r/ancientrome/comments/134fxfy/your_opinions_about_roman_emperors_xlvii_galerius/",
         "https://www.reddit.com/r/ancientrome/comments/136faon/your_opinions_about_roman_emperors_xlix_after_a/",
         "https://www.reddit.com/r/ancientrome/comments/138drl3/your_opinions_about_roman_emperors_li_constantius/",
         "https://www.reddit.com/r/ancientrome/comments/139ihol/your_opinions_about_roman_emperors_lii_julian_ii/",
         "https://www.reddit.com/r/ancientrome/comments/13ail3j/your_opinions_about_roman_emperors_liii_jovian/",
         "https://www.reddit.com/r/ancientrome/comments/13bjz9w/your_opinions_about_roman_emperors_liv/",
         "https://www.reddit.com/r/ancientrome/comments/13ck20b/your_opinions_about_roman_emperors_lv_valens/",
         "https://www.reddit.com/r/ancientrome/comments/13djxg6/your_opinions_about_roman_emperors_lvi_gratian/",
         "https://www.reddit.com/r/ancientrome/comments/13egkh7/your_opinions_about_roman_emperors_lvii/",
         "https://www.reddit.com/r/ancientrome/comments/13fbtum/your_opinions_about_roman_emperors_lviii_western/",
         "https://www.reddit.com/r/ancientrome/comments/13gc10l/your_opinions_about_roman_emperors_lix/",
         "https://www.reddit.com/r/ancientrome/comments/13ic03e/your_opinions_about_roman_emperors_lxi/",
         "https://www.reddit.com/r/ancientrome/comments/13izonp/your_opinions_about_roman_emperors_lxii/",
         "https://www.reddit.com/r/ancientrome/comments/13juat6/your_opinions_about_roman_emperors_lxiii/",
         "https://www.reddit.com/r/ancientrome/comments/13kpy7j/your_opinions_about_roman_emperors_lxiv_petronius/",
         "https://www.reddit.com/r/ancientrome/comments/13lm0ch/your_opinions_about_roman_emperors_lxv_avitus/",
         "https://www.reddit.com/r/ancientrome/comments/13ml6lb/your_opinions_about_roman_emperors_lxvi_maiorianus/",
         "https://www.reddit.com/r/ancientrome/comments/13nmcvq/your_opinions_about_roman_emperors_lxvii_libius/",
         "https://www.reddit.com/r/ancientrome/comments/13ohivk/your_opinions_about_roman_emperors_lxviii/",
         "https://www.reddit.com/r/ancientrome/comments/13pivir/your_opinions_about_roman_emperors_lxix_olibrius/",
         "https://www.reddit.com/r/ancientrome/comments/13qhdnp/your_opinions_about_roman_emperors_lxx_glicerius/",
         "https://www.reddit.com/r/ancientrome/comments/13r9ges/your_opinions_about_roman_emperors_lxxi_julius/"
         
         
         
         
         
         
         
         
         ]

names = {}

votes = {}

# Sometimes the URLs don't include the name of the emperor, this is a correction list
spare = ["lxviii", "lxiii", "lxii", "lxi", "lix", "western" , "lvii", "liv", "ii" , "a", "the" , "xxxxtacitus", "xxxviii"
         , "xxxvii" , "xxxiv", "xxxiii", "iii", "gordian", "i" , "we", "xxiii"]

    
for url in links:

    page = rq.urlopen(url)

    readit = str(page.read())
    
    # Back before I knew of the existence of BeautifulSoup, life was much harder and sadder. :(     
    # A crappy parsing loop to find all the vote counts       
    str_index = -2
    numbers = []
    current_text = readit

    while str_index != -1:
        
        # This is just a crappy way to find the number of votes, ignore this code and just think of it as extracting the number of votes
        str_index = current_text.find("number=\"")
        
        search_range = current_text[str_index-20:str_index+20]
        
        part1 = search_range.find("\"")
        
        search_range = search_range[part1+1:]
        
        part2 = search_range.find("\"")
        search_range = search_range[:part2:]
        

        try:
        
            numbers.append(int(search_range))
        except:
            # I don't remember if it failed in the end or not, but I am keeping it since there won't be any more modifications made to this program
            pass
        
        current_text = current_text[str_index+10:]
        
    # The first 2 numbers are not the vote counts
    numbers = numbers[2:]

    # If only I knew what BeautifulSoup was...
    emp_name = url[:len(url)-1:].split("_")[-1]
    
    print("emperor: " , emp_name)
    

    total = 0

    # Calculating weighted mean
    for i in range(5,1-1,-1):
        total += i * numbers[5-i+1]
        
    votes.update({ emp_name : numbers[0] })
        
    mean = round(total / numbers[0], 2)

    if emp_name in spare: 
        names.update({emp_name : mean})
    else:
        names.update({emp_name + f" ({mean}, {numbers[0]} votes)": mean})
    


# Correcting all the names
    
names.update({f"galba ({names['we']}, {votes['we']} votes)" : names["we"]})    

del names["we"] 

names.update({f"gordian I ({names['i']}, {votes['i']} votes)" :  names["i"]})

del names["i"]

names.update({f"gordian II ({names['gordian']}, {votes['gordian']} votes)" : names["gordian"]})

del names["gordian"]

names.update({f"gordian III ({names['iii']}, {votes['iii']} votes)" :  names["iii"]})

del names["iii"]

names.update({f"elegabalus ({names['xxiii']}, {votes['xxiii']} votes)" : names["xxiii"]})

del names["xxiii"]

names.update({f"trebonianus gallus ({names['xxxiii']}, {votes['xxxiii']} votes)" : names["xxxiii"]})

del names["xxxiii"]

names.update({f"aemilianus ({names['xxxiv']}, {votes['xxxiv']} votes)" : names["xxxiv"]})

del names["xxxiv"]

names.update({f"claudius gothicus ({names['xxxvii']}, {votes['xxxvii']} votes)" : names["xxxvii"]})

del names["xxxvii"]

names.update({f"quintillus ({names['xxxviii']}, {votes['xxxviii']} votes)" : names["xxxviii"]})

del names["xxxviii"]

names.update({f"tacitus ({names['xxxxtacitus']}, {votes['xxxxtacitus']} votes)" : names["xxxxtacitus"]})

del names["xxxxtacitus"]

names.update({f"maximilianus ({names['the']}, {votes['the']} votes)" : names["the"]})

del names["the"]

names.update({f"constantine I ({names['a']}, {votes['a']} votes)" : names["a"]})

del names["a"]

names.update({f"julian II ({names['ii']}, {votes['ii']} votes)" : names["ii"]})

del names["ii"]

names.update({f"valentinian I ({names['liv']}, {votes['liv']} votes)" : names["liv"]})

del names["liv"]

names.update({f"theodosius I ({names['lvii']}, {votes['lvii']} votes)" : names["lvii"]})

del names["lvii"]

names.update({f"magnus maximus ({names['western']}, {votes['western']} votes)" : names["western"]})

del names["western"]

names.update({f"valentinian II ({names['lix']}, {votes['lix']} votes)" : names["lix"]})

del names["lix"]

names.update({f"constantine III ({names['lxi']}, {votes['lxi']} votes)" : names["lxi"]})

del names["lxi"]

names.update({f"constantius III ({names['lxii']}, {votes['lxii']} votes)" : names["lxii"]})

del names["lxii"]

names.update({f"valentinianus III ({names['lxiii']}, {votes['lxiii']} votes)" : names["lxiii"]})

del names["lxiii"]

names.update({f"anthemius ({names['lxviii']}, {votes['lxviii']} votes)" : names["lxviii"]})

del names["lxviii"]

# Filling in the ones I couldn't add

names.update({f"augustus (4.31, 267 votes)" : 4.31 })

names.update({f"vespasian (4.12, 588 votes)" : 4.12 })

names.update({f"Marcus aurelius (4.47, 354 votes)" :  4.47 })

names.update({f"chlorus (3.29, 65 votes)" : 3.29 })

names.update({f"licinius (3.04, 50 votes)" : 3.04 })

names.update({f"honorius (1.89, 63 votes)" : 1.89 })

names.update({f"Romulus augustulus (2.56, 100 votes)" : 2.56 })

# Sort the names
names = dict(sorted(names.items(), key=lambda x:x[1], reverse= True  ))

# Plotting time

from matplotlib import pyplot as plt
import numpy as np
import matplotlib.colors as mcolors


# Colour map I ripped off from someone on stackoverflow

cdict = {'red':  ((0.0, 0.0, 0.0),
                (1/6., 0.0, 0.0),
                (1/2., 0.8, 1.0),
                (5/6., 1.0, 1.0),
                (1.0, 0.4, 1.0)),

            'green':  ((0.0, 0.0, 0.4),
                (1/6., 1.0, 1.0),
                (1/2., 1.0, 0.8),
                (5/6., 0.0, 0.0),
                (1.0, 0.0, 0.0)),

            'blue': ((0.0, 0.0, 0.0),
                (1/6., 0.0, 0.0),
                (1/2., 0.9, 0.9),
                (5/6., 0.0, 0.0),
                (1.0, 0.0, 0.0))

    }

my_cmap=mcolors.LinearSegmentedColormap('rg',cdict, N=256).reversed()

my_cmap2=mcolors.LinearSegmentedColormap.from_list('rg',["red", "orange", "lime"], N=256) 

# Sanity checks
print(type(names))

print(names)

# This is the largest font size I could add that doesn't clip
plt.rcParams.update({"font.size" : 8})

fig, ax = plt.subplots(ncols= 1 , nrows = 1, figsize=(1920*px,1080*px))

# Plotting the bars
ax.barh([ x.capitalize() for x in  list(names.keys()) ], [ x-1 for x in list( names.values()    )], 
        height=0.6, 
        color = my_cmap([(x-0.5)/5 for x in list(names.values())]) )

ax.set_title("Ranking Roman Emperors - Best to Worst", fontsize =21)

ax.set_xlabel("Mean score", fontsize = 18)

number_scores = list(names.values())

# Median = 3.04
print(number_scores[int((len(number_scores)-1)/2)])

ax.invert_yaxis()

ax.set_xticks([0,1,2,3,4])
ax.set_xticklabels(["1 (highly negative)", "2 (negative)" , "3 (neutral)" , "4 (positive)" , "5 (highly positive)"])


ax.axvline(x=2.04, color="blue", linestyle="dotted")
ax.text(2.69/5, 0.5, "Median (3.04)" , transform=ax.transAxes, fontsize=10, color="blue")



plt.savefig("romans.png")

plt.show()


    
    
        
    
    

    



