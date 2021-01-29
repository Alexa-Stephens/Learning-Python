#in this program, the user will enter their birthdate, and learn what their zodiac sign is

def calculatezodiac():
    #get zodiac input
    date = str(input("Please enter your birth date in format MM/DD:   "))
    print("Here is the date you entered: ", str(date))
    
    #check formatting
    slash = date[2]
    if slash != '/':
        print("Date not entered correctly. Please use format MM/DD")
        return
    
    # check if date is valid
    #get birth month and birth date
    birthmonth = date[:2]
    birthdate = date[3:5]

    #test birth month
    if birthmonth < "01" or birthmonth> "12":
        print("Birth month not valid.")
        return
    
    #test birthdate
    if birthdate > "31":
        print("Birth date not valid.")
        return
    elif (birthmonth == "04" or birthmonth == "06" or birthmonth == "09" or birthmonth == "11") and birthdate == "31":
        print("Birth date not valid.")
        return
    elif (birthmonth == "02") and birthdate == "30":
        print("Birth date not valid.")
        return
    
    
    
    #calculate zodiac
    
    #
      #  Aries : March 21 - April 19
      #  Taurus : April 20 - May 20
      #  Gemini : May 21 - June 20
      #  Cancer : June 21 - July 22
      #  Leo : July 23 - August 22
      #  Virgo : August 23 - September 22
      #  Libra : September 23 - October 22
      #  Scorpio : October 23 - November 21
      #  Sagittarius : November 22 - December 21
      #  Capricorn : December 22 - January 19
      #  Aquarius : January 20 - February 18
      #  Pisces : February 19 - March 20
    
    if date>="03/21" and date<="04/19":
        print("Aries")
    elif date>="04/20" and date<= "05/20":
        print("Taurus")
    elif date>="05/21" and date<="06/20":
        print("Gemini")
    elif date>="06/21" and date<="07/22":
        print("Cancer")
    elif date>="07/23" and date<="08/22":
        print("Leo")
    elif date>="08/23" and date<="09/22":
        print("Virgo")
    elif date>="09/23" and date<="10/22":
        print("Libra")
    elif date>="10/23" and date<="11/21":
        print("Scorpio")
    elif date>="11/22" and date<="12/21":
        print("Sagittarius")
    elif date>="12/22" and date<="12/31":
        print("Capricorn")
    elif date>="01/01" and date<="01/19":
        print("Capricorn")
    elif date>="01/20" and date<="02/18":
        print("Aquarius")
    elif date>="02/19" and date<="03/20":
        print("Pisces")
    else:
        print("Date entered incorrectly")

calculatezodiac()
