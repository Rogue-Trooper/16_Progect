import string
str = """This year, Tim Burton received the prestigious Lumière Award, which pays tribute to a great name in cinema in Lyon each year.
He joins a distinguished list of predecessors including, Quentin Tarantino, Pedro Almodovar, and from last year, Jane Campion.
A real success and proof of the public's love for the American filmmaker who has made some of cinema's masterpieces, from 'Batman' to 'Alice in Wonderland', via 'Edward Scissorhands' and 'Charlie and the Chocolate Factory', the list is long.
He got a rock star welcome in Lyon, especially during his visit to the Institut Lumière, on the very spot where the Lumière brothers shot the first film in the history of cinema, 'La Sortie des Usines Lumière'.
"I am a primitive person. When I started making my little super-eight films, that's why I love stop-motion, I love the sort of artistry, and it goes back to the beginning of film, and it was like magic. So what better place to be it's great, to kind of feel the energy of this place is amazing".
Tim Burton 
Film Director
Incredible energy and rooms filled to the brim like the Halle Tony-Garnier transformed into the largest indoor cinema in the world with its 5000 seats for Tim Burton Night.
As well as nearly 500 screenings at the festival, there were also masterclasses like the one given by Monica Bellucci, who spoke at length about her career as an actress and her latest film, The Girl in the Fountain, dedicated to another icon of the cinema, Anita Ekberg.
Euronews
Anita Ekberg in La Dolce VitaEuronews
The Girl in the Fountain premieres during the Lumière Festival, an ideal location for a film that combines fact and fiction, past and present.
"Tim Burton reminds me a lot of Fellini because he is someone who draws a lot, and these films really allow us to dream and to rise up I think...".
Monica Bellucci 
Actress
"The Lyon Festival is a heritage festival. You can watch films where there are so many archives in them, historical films, restored films, and this allows young people to stay in touch with the past, with what has made and continues to make the strength of cinema and art". Said Monica Bellucci.
There were many retrospectives during the Lumière Festival, including that of the American filmmaker James Gray, who also came with his latest film, 'Armageddon Time'.
"It's going to take a concerted effort over many years to try to keep making films that push the envelope a little bit and then just hope that the audience comes back. On that, I have a little optimism because I feel as though there's always room for something different".
James Gray 
American Filmmaker
The semi-autobiographical story of his childhood in Queens New York, where he was confronted with anti-Semitism, segregation, and social inequality.
James Gray is a demanding author who, despite the pressure of the big studios and platforms, manages to deliver personal films that remain popular.
The 14th Festival Lumière ended in triumph and a standing ovation for Tim Burton, who left Lyon with stars in his eyes."""

d = {}
alfabet = string.ascii_lowercase
s = str.lower()

for ch in alfabet:
    d[ch] = s.count(ch)

# for key, value in d.items():
#     print(key, " - ", value)

max_key = "a"
min_key = "a"

for key in d:
    if d[key] > d[max_key]:
        max_key = key

    if d[key] < d[min_key]:
        min_key = key

print(max_key, " - ", d[max_key])
print(min_key, " - ", d[min_key])

