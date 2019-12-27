"""
Vigener encryptor, decryptor and a statistical attack on vigener encrypted text
"""

def eve(Text,Key):
    charText=[x for x in Text]
    charKey=[y for y in Key]
    keyLength=len(charKey)
    for k in range(26):
        i=0
        for t in charText:
            if t.isalpha():
                if ord(t)>=ord('a'):
                    print(chr(((ord(t.lower())-ord(charKey[i%keyLength]))%26+ord('a'))), end="")
                else:
                    print(chr(((ord(t.lower())-ord(charKey[i%keyLength]))%26+ord('A'))), end="")
                i=i+1
            else:
                print(t, end="")
        for x in range(keyLength):
            charKey[x] = chr(((ord(charKey[x])+1)-ord('a'))%26+ord('a'))
        print("")
        print("")


def bob(Text,Key1,Key2):
    charText=[x for x in Text]
    charKey=[y for y in Key1]
    keyLength=len(charKey)
    for x in range(keyLength):
        charKey[x] = chr(((ord(charKey[x])+Key2)-ord('a'))%26+ord('a'))
    i=0
    for t in charText:
        if t.isalpha():
            if ord(t)>=ord('a'):
                print(chr(((ord(t.lower())+ord(charKey[i%keyLength])-2*ord('a'))%26+ord('a'))), end="")
            else:
                print(chr(((ord(t.lower())+ord(charKey[i%keyLength])-2*ord('a'))%26+ord('A'))), end="")
            i=i+1
        else:
            print(t, end="")
    print("")


'''
coincidenceIndex: Συνάρτηση που υπολογίζει τον δείκτη σύμπτωσης σε ένα δοσμένο κείμενο ή πίνακα
'''
def coincidenceIndex(Text):
    length = len(Text)
    result=0
    freq = [0]*26 #Πίνακας συχνοτήτων
    for i in Text:
        freq[ord(i)-ord('A')]=freq[ord(i)-ord('A')]+1
    for i in freq:
        result = result + (i*(i-1))/(length*(length-1)) #υπολογιζμός πιθανότητας
    return result

'''
vigener: Συνάρτηση που παίρνει σαν είσοδο ένα κρυπτοκείμενο που προέκυψε με
         Vigener cipher και βγάζει 26 διαφορετικές εκδοχές για το αρχικό κείμενο
         και το κλειδί
'''
def vigener(Text):
    ltext=coincidenceIndex(Text) #Coincidence Index of original text
    charText=[x for x in Text]
    meanIndexes = [] #Πίνακας που θα αποθηκευτούν οι μέση όροι των CI για διαφορετικό μήκος κλειδιού
    possibleKeyLength= round((0.065-0.038)/(ltext-0.038)) #Εύρεση πιθανού μήκους κλειδιού με χρήση του τύπου
    for i in range(possibleKeyLength*2): #Επειδή ο τύπος είναι πιθανοτικός ψάχνω σε μια περιοχή γύρω από το πιθανό μήκος κλειδιού
        temp=0
        for x in range(i+1):
            temp=temp+coincidenceIndex(charText[x::(i+1)])
        meanIndexes.append(temp/(i+1)) #κρατάω τον μέσω δείκτη σύμπτωσης των διαφορετικών ομάδων
    keyLength=  meanIndexes.index(max(meanIndexes))+1 #παίρνω μήκος κλειδιού ίσο με αυτό που έχει τον μεγαλύτερο μέσο CI
    shiftList= []
    list1=charText[1::keyLength]
    for i in range(keyLength): #Βρίσκω σχετικές ολισθήσεις με την δεύτερη ομάδα γραμμάτων list1
        list2=charText[i::keyLength]
        index=0
        shift=[]
        for k in range(26): #Βρίσκω για όλες τις ολισθήσεις τους CI και κρατάω τον καλύτερο
            index = coincidenceIndex(list2+list1)
            shift.append(index)
            for x in range(len(list2)):
                list2[x] = chr(((ord(list2[x])-1)-ord('A'))%26+ord('A')) #ολισθαίνω κατα -1 την ομάδα γραμμάτων
        shiftList.append(shift.index(max(shift)))
    key=[0]
    for i in range(keyLength-1): #βρίσκω ένα πιθανό κλειδί που ικανοποίει τις ολισθήσεις
            key.append((shiftList[i+1]-shiftList[0])%26)
    for k in range(26): #τυπώνω 26 διαφορετικές ολισθήσεις του κλειδιού και το αντίστοιχο κείμενο
        i=0
        for t in charText:
                print(chr(((ord(t)-key[i%keyLength]-ord('A'))%26+ord('A'))), end="") #ολισθαίνω τα γράμματα ανάλογα με το κλειδί
                i=i+1
        print("")
        print("")
        for x in range(keyLength): #ολισθαίνω το κλειδί και το τυπώνω
            key[x] = (key[x]+1)%26
            print(chr(key[x]+ord('A')), end="")
        print("")
        print("")


if __name__ == "__main__":
    print("Exercise 1.2")
    eve("Nd Gob. A njrm ejoim mesd ri alxk jwmpekmxxo Gbz lnpl izx. Bq aup txxdvt pbvg zcg Ofyoiik nkvcgk, tw mjyeo wyz c Hkw Ddqx Acj vriogkxl ptvn v ttkvyh oxj vnvv bp sd gitdv gn dbd sc jyk xgynczb.","cryptography")
    print("")
    print("Exercise 1.3")
    bob("Hi Eve. I dont think that we have outsmarted Eve just yet. If you really like the Vigener cipher, we could use a One Time Pad approach with a random key that is at least as big as our message.","cryptography",4)
    print("")
    print("Exercise 2")
    vigener("VVTWZARYOORLVUGHRBPQFCFDDYWGFLSELQEVOEBTARTFTWLBVUUOLFXBPBSXDJHVAHTAIFUPNVZNTTLESEPRDPTIPZAGZSDQURPDHDQMNTAHTHILQMHJXIARYOVCMFUAHTSIGGVFBPVJKSLELAFCUDSTKGCAOGDLVGHNSEPRRVWTCBUGFTDZSSTVMISMCGVPAPEVNSRTECEPAOISMCGVPAPIAFZOAZVTCZMTYLVGSIQPZGADIAWVRXLREPZVUO")
