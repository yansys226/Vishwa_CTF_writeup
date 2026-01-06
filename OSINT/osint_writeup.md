# **Rocket Raccoon**

We need to find 'racckoonn' and information about their owner as they apparently leaked private information.

The first thing we found was a racckoon account on instagram: <https://dumpor.com/v/racckoonn>.

In one of the photo descriptions we can find this quote:

> Check out my mum's new YouTube channel!
> https://www.youtube.com/channel/UCDurVPcUypifNkJVrHxJ3vQ

Going to <https://www.youtube.com/channel/UCDurVPcUypifNkJVrHxJ3vQ> reveals that the mom's youtube account name is `JohnsonM3llisa`.

Unfortunately it doesn't seem that there is anything of relevance on this youtube channel, no videos and no descriptions of any sorts.

Though with a bit of digging, we found an account on twitter with a similar name: <https://twitter.com/JohnsonM3llisa>.  
And there is a peculiar tweet that reads:

> OOPS! Almost leaked some private information, hope there is no way to get it back haha

This does hint us that using something like the wayback machine may yield some results: <https://web.archive.org/>.

And looking at the snapshots, we got a hit: <https://web.archive.org/web/20220315110835/https://twitter.com/JohnsonM3llisa>.

The flag is given to us in a tweet:

> Good job
> Here's your flag
> Vishwactf{R4cc00ns_4r3_Sm4rt}

The flag we submitted was: **Vishwactf{R4cc00ns_4r3_Sm4rt}**

---

# **The Library** (We almost solved it during the event, just got blocked at the last hurdle)

To start the challenge, we need to send a private message "Hello" To the Librarian bot on the CTF's discord.

Their first question:
```
Welcome! Bring me what I ask and I shall take you on a journey across the land of books.
Here is the first step -
'Very few of us are what we seem.'
Tommy is to call on Miss Glen at what time? Give me the time in 12 hr format (HH:MM) (without am/pm) and I will lead you further.
```

The quote seems to come from Aghatha Christie from the book "Man in the Mist" <https://www.goodreads.com/quotes/666981-very-few-of-us-are-what-we-seem>.

A bit of googling and seeking quotes gave me the time:

<https://www.google.com/search?q=the+man+in+the+mist+agatha+christie+tommy+is+to+call+glenn&rlz=1C1SQJL_enFR934FR934&biw=1920&bih=937&sxsrf=APq-WBs1yQPDHlkYXSn4Xk-cs6KScj1oRA%3A1648638625739&ei=oTpEYrnRLMKWjgb47IuIBg&ved=0ahUKEwj5pZm92e32AhVCi8MKHXj2AmEQ4dUDCA4&uact=5&oq=the+man+in+the+mist+agatha+christie+tommy+is+to+call+glenn&gs_lcp=Cgdnd3Mtd2l6EAM6BwgjELADECdKBAhBGAFKBAhGGABQhQ1YwxdguxxoAnAAeACAAWmIAesHkgEDOS4ymAEAoAEByAECwAEB&sclient=gws-wiz>

<https://en.wikipedia.org/wiki/Partners_in_Crime_(short_story_collection)>

> Bulger tells them that she is engaged to marry Lord Leconbury, who meets the actress outside the door to the hotel. Bulger leaves soon afterwards and Tommy receives a note from Miss Glen asking for his help and for him to call on her at The White House, Morgan's Avenue, at 6.10 pm.

The awnser is "06:10".

Second question:

```
Good job, here is the next part -
He appeared to help the Son of Neptune, this seer has a history of helping heroes on their quests. He is also acknowledged in mythology to guide a voyage to retrieve what?
```

A quick google search points us to Phineas as the seer: <https://riordan.fandom.com/wiki/Phineas>.

This blog post <https://www.greekmythology.com/Myths/Mortals/Phineus/phineus.html> seems to point the object as being the Golden Fleece.

The awnser is "Golden Fleece".

Third question:

```
Well done, here is the next part -
'The year without a summer, a vacation, and a classic was created.'
 In this classic, the names of the creation and creator are often confused. Give me the name of the university where the creator studied and I shall give you the next piece of the puzzle.
```

The book referenced by the hint seems to be Frankenstein.

Going on their wikipedia <https://en.wikipedia.org/wiki/Frankenstein> and CTRL-F for the word University, we got a hit on "University of Ingolstadt".

This is our Third awnser.

Fourth question:
```
Splendid, here is the next part -
```
![runes](./Library/runes.jpg)
```
What is the name of the dragon?
```

Looking at the list of symbol ciphers on dcode: <https://www.dcode.fr/symbols-ciphers>.

We found the Elder Futhark to be the closest match for our text.  
After a lot of struggle we found a quote from the hobbit (lost the quote but it was hell to decode it).

The dragon in the hobbit is "Smaug".

This is our fourth awnser.

Fith question (the one we got stuck on):

```
Great job on persevering, this is the last part -
```
![pigpen](./Library/pigpen.jpg)
```
These Symbols might make you feel pretty Lost, but not as much as a severed hand right in the
```
![cathedral](./Library/cathedral.jpg))
```
Give me the deciphered text and I shall give you the flag.
```

We identified that the cipher was a pigpen Cipher using the list of symbol ciphers from earlier (<https://www.dcode.fr/symbols-ciphers>)

Directly deciphering the text gives us this string: `NISYTETPRISTNUFO`. But it wasn't the awnser.

Looking the cathedral image up gives us this <https://www.aoc.gov/explore-capitol-campus/buildings-grounds/capitol-building/rotunda>.

This is where we got stuck during the event and nothing that we did with the text seemed to work.

---

# **Caught Very Easily**

To solve this challenge we are looking for an entry on the Exploit Database website (<https://www.exploit-db.com/>).

The hints provided in the description are the name of an important individual, Ahmed Mansoor and the keyword JAILBREAK.

Looking up quickly "mansoor jailbreak" on google, we can find several articles. The one we found helpful was this one: <https://citizenlab.ca/2016/08/million-dollar-dissident-iphone-zero-day-nso-group-uae/>.

It includes several CVE entries which are the different vulnerabilities used to do the exploit.

Looking one of them up (the CVE-2016-4655 for example): <https://nvd.nist.gov/vuln/detail/CVE-2016-4655>  
We can find details about the vulnerability and in the references below, there is an exploit-db link: <https://www.exploit-db.com/exploits/44836/>

It looks like we hit our jackpot, putting the informations in our flag format we obtain: **vishwaCTF{44836_2018-06-05}**
