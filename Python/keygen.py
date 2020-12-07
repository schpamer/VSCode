import numpy as np

    #string str1 = this.textBoxUsername.Text.TrimEnd();
    #int int32 = Convert.ToInt32(this.textBoxDays.Text);
    #this.nToStop = 0;
    #this.nCounter = 0;
    #this.bContinue = true;
    #this.ssOut = "";

strdate = 50

#set basic error checkling
    if strdate.Length < 3:
        print("Username must be more than 2 characters!")

    elif strdate <= 15 or strdate > 3650
        print("Activation Days must be between 15 and 3650!")
    
    elif isdigit(strdate)
        print("")

#this calculates str1 by the algo below
    else:

    def DoR(string s)
        char[] charArray = s.ToCharArray();
            Array.Reverse((Array) charArray);
        for (int index = 0; index < charArray.Length; ++index)
              charArray[index] = (char) ((uint) charArray[index] + 1U);
        return new string(charArray).ToLower();
    }

# This is for day calculations so poss integer number in to matrix if number falls in category then categorize it and return "X" + ToR(...)
     def ToR(number)
    
      if (number < 0 or number > 3999)
        return "";
      if (number < 1)
        return string.Empty;
      if (number >= 1000)
        return "M" + this.ToR(number - 1000);
      if (number >= 900)
        return "CM" + this.ToR(number - 900);
      if (number >= 500)
        return "D" + this.ToR(number - 500);
      if (number >= 400)
        return "CD" + this.ToR(number - 400);
      if (number >= 100)
        return "C" + this.ToR(number - 100);
      if (number >= 90)
        return "XC" + this.ToR(number - 90);
      if (number >= 50)
        return "L" + this.ToR(number - 50);
      if (number >= 40)
        return "XL" + this.ToR(number - 40);
      if (number >= 10)
        return "X" + this.ToR(number - 10);
      if (number >= 9)
        return "IX" + this.ToR(number - 9);
      if (number >= 5)
        return "V" + this.ToR(number - 5);
      if (number >= 4)
        return "IV" + this.ToR(number - 4);
      if (number >= 1)
        return "I" + this.ToR(number - 1);
      return "";
    }