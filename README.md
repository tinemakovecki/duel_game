# Duel Game
Igra za projekt pri predmetu Programiranje 2

## Opis
Igra je zasnova na konceptu bitk v pokemon igrah. Dva nasprotnika se izmenično napadata, dokler enemu ne zmanjka življenskih točk.

## Načrt dela
* 22.3. - 29.3. Koncept igre, načrtovanje, vzpostavitev repozitorija
* 29.3. - 5.4. Osnove grafičnega vmesnika
* 5.4. - 12.4. Dodelava grafičnega vmesnika
* 12.4. - 19.4. Logika igre
* 19.4. - 26.4 Igranje za človeške igralce, osnove računalniškega igralca
* 26.4. - 3.5. Dodelava igre proti računalniku, popravki
* 3.5. - 10.5. Testiranje, dodatki

## Igranje
Za začetek igre poženemo datoteko `GUI.py`. Odpre se nam začetno okno, v katerem lahko za oba igralca izberemo ali ju bo igral človek ali računalnik. Igra se začne, ko pritisnemo gumb Start new game. 
V zgornjem levem kotu imamo glavni meni `Game`, v katerem so možnosti `Help` - odpre nam navodila igre; `New Game` - vrže nas nazaj na začetno okno, kjer lahko ponovno izberemo igralca; `Quit` - izhod iz igre. 
Igralca se izmenično napadata, dokler enemu ne zmanjka življenskih točk. Takrat se nam odpre končno okno, ki nam pove kdo je zmagovalec, ter nam da možnost ponovne igre.

## Datoteke
* **GUI.py:** uporabniški vmesnik, ki ga zaženemo, da začnemo igrati. Izriše nam začetno, igralno in končno okno, ter nas obvešča o poteku igre.
* **Game.py:** logika igre, ki poskrbi, da se, ko igralec izbere napad, le ta izvede. Preverja stanje igre, izračuna škodo, ter posodablja modifikatorje. Za potrebo minimax algoritma naredi kopijo igre, z možnostjo razveljavitve poteze.
* **Class.py:** v tej datoteki se nahajata razreda `Attack` - ime, škoda, možnost zadetka in modifikatorji za posamezni napad, ter `Monster` - ime, življenske točke in napadi za posamezno pošast, konstruktorja, ki naredita pošasti `Pikachu` in `Charmander` in funkciji za kopijo pošasti ter možne napade.
* **Player.py:** ustvari človeškega igralca
* **Computer.py:** ustvari računalniškega igralca. Ta igra s pomočjo algoritma `Minimax`.
* **Minimax.py:** tu se nahaja algoritem, s pomočjo katerega igra računalniški igralec. 
* **Help.py:** vsebuje opis igrice in navodila.
