{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hashim\n",
      "Sami\n",
      "69\n",
      "karachi\n",
      "High Acadmic Level\n",
      "{'first_name': 'Hashim', 'last_name': 'Sami', 'age': 69, 'city': 'karachi'}\n"
     ]
    }
   ],
   "source": [
    "person = {\n",
    "    'first_name': 'Hashim',\n",
    "    'last_name': 'Sami',\n",
    "    'age': 69,\n",
    "    'city': 'karachi',\n",
    "    }\n",
    "\n",
    "print(person['first_name'])\n",
    "print(person['last_name'])\n",
    "print(person['age'])\n",
    "print(person['city'])\n",
    "person.update( {'qualification' : 'High Acadmic Level'} )\n",
    "print(person['qualification'])\n",
    "del person['qualification']\n",
    "print(person)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Karachi is in Pakistan.\n",
      "  It has a population of about 6158080.\n",
      "  The K2 mountains are nearby.\n",
      "\n",
      "Hong Kong is in China.\n",
      "  It has a population of about 876.\n",
      "  The K2 Range mountains are nearby.\n",
      "\n",
      "Kathmandu is in Nepal.\n",
      "  It has a population of about 1003285.\n",
      "  The Himilaya mountains are nearby.\n"
     ]
    }
   ],
   "source": [
    "cities = {\n",
    "    'Karachi': {\n",
    "        'country': 'Pakistan',\n",
    "        'population': 6158080,\n",
    "        'nearby mountains': 'K2',\n",
    "        },\n",
    "    'Hong Kong': {\n",
    "        'country': 'China',\n",
    "        'population': 876,\n",
    "        'nearby mountains': 'K2 range',\n",
    "        },\n",
    "    'kathmandu': {\n",
    "        'country': 'nepal',\n",
    "        'population': 1003285,\n",
    "        'nearby mountains': 'himilaya',\n",
    "        }\n",
    "    }\n",
    "\n",
    "for city, city_info in cities.items():\n",
    "    country = city_info['country'].title()\n",
    "    population = city_info['population']\n",
    "    mountains = city_info['nearby mountains'].title()\n",
    "\n",
    "    print(\"\\n\" + city.title() + \" is in \" + country + \".\")\n",
    "    print(\"  It has a population of about \" + str(population) + \".\")\n",
    "    print(\"  The \" + mountains + \" mountains are nearby.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "How old are you?\n",
      "Enter 'quit' when you are finished. 20\n",
      "  Your ticket is $15.\n",
      "How old are you?\n",
      "Enter 'quit' when you are finished. quit\n"
     ]
    }
   ],
   "source": [
    "prompt = \"How old are you?\"\n",
    "prompt += \"\\nEnter 'quit' when you are finished. \"\n",
    "\n",
    "while True:\n",
    "    age = input(prompt)\n",
    "    if age == 'quit':\n",
    "        break\n",
    "    age = int(age)\n",
    "\n",
    "    if age < 3:\n",
    "        print(\"  You get in free!\")\n",
    "    elif age < 13:\n",
    "        print(\"  Your ticket is $10.\")\n",
    "    else:\n",
    "        print(\"  Your ticket is $15.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Quran is one of my favorite books.\n"
     ]
    }
   ],
   "source": [
    "def favorite_book(title):\n",
    "    \"\"\"Display a message about someone's favorite book.\"\"\"\n",
    "    print(title + \" is one of my favorite books.\")\n",
    "\n",
    "favorite_book('Quran')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Take a Guess11\n",
      "Your guess is too high.\n",
      "Take a Guess10\n",
      "Your guess is too high.\n",
      "Take a Guess4\n",
      "Your guess is too high.\n",
      "Nope. The Correct Number is 1\n"
     ]
    }
   ],
   "source": [
    "# This is a guess the number game.\n",
    "import random\n",
    "guessesTaken = 0\n",
    "number = random.randint(1, 30)\n",
    "while guessesTaken < 3:\n",
    "           guess = int(input('Take a Guess'))\n",
    "           guessesTaken = guessesTaken + 1\n",
    "           if guess < number:\n",
    "                 print('Your guess is too low.') # There are eight spaces in front of print.\n",
    "           if guess > number:\n",
    "                 print('Your guess is too high.')\n",
    "           if guess == number:\n",
    "                 print('Your guess is too high.')\n",
    "                 break\n",
    " \n",
    "if guess != number:\n",
    "    number = str(number)\n",
    "    print('Nope. The Correct Number is ' + number)                   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
