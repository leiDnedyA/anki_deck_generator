import filter
import anki

def main():
    text = "1 comme	as 2	je	I 3	son	his 4	que	that 5	il	he 6	était	was 7	pour	for 8	sur	on 9	sont	are 10	avec	with 11	ils	they 12	être	be 13	à	at 14	un	one 15	avoir	have 16	ce	this 17	à_partir_de	from 18	par	by 19	chaud	hot 20	mot	word 21	mais	but 22	que	what 23	certains	some 24	est	is 25	il	it 26	vous	you 27	ou	or 28	eu	had 29	la	the 30	de	of 31	à	to 32	et	and 33	un	a 34	dans	in 35	nous	we 36	boîte	can 37	dehors	out 38	autre	other 39	étaient	were 40	qui	which 41	faire	do 42	leur	their 43	temps	time 44	si	if 45	volonté	will 46	comment	how 47	dit	said 48	un	an 49	chaque	each 50	dire	tell 51	ne	does 52	ensemble	set 53	trois	three 54	vouloir	want 55	air	air 56	bien	well 57	aussi	also 58	jouer	play 59	petit	small 60	fin	end 61	mettre	put 62	maison	home 63	lire	read 64	main	hand 65	port	port 66	grand	large 67	épeler	spell 68	ajouter	add 69	même	even 70	terre	land 71	ici	here 72	il_faut	must 73	grand	big 74	haut	high 75	tel	such 76	suivre	follow 77	acte	act 78	pourquoi	why 79	interroger	ask 80	hommes	men 81	changement	change 82	est_allé	went 83	lumière	light 84	genre	kind 85	de	off 86	besoin	need 87	maison	house 88	image	picture 89	essayer	try 90	nous	us 91	encore	again 92	animal	animal 93	point	point 94	mère	mother 95	monde	world 96	près_de	near 97	construire	build 98	soi	self 99	terre	earth 100	père	father 101	tout	any 102	nouveau	new 103	travail	work 104	partie	part 105	prendre	take 106	obtenir	get 107	lieu	place 108	fabriqué	made 109	vivre	live 110	où	where 111	après	after 112	arrière	back 113	peu	little 114	seulement	only 115	tour	round 116	homme	man 117	année	year 118	est_venu	came 119	montrer	show 120	tous	every 121	bon	good 122	moi	me 123	donner	give 124	notre	our 125	sous	under 126	nom	name 127	très	very 128	par	through 129	juste	just 130	forme	form 131	phrase	sentence 132	grand	great 133	penser	think 134	dire	say 135	aider	help 136	faible	low 137	ligne	line 138	différer	differ 139	tour	turn 140	la_cause	cause 141	beaucoup	much 142	signifier	mean 143	avant	before 144	déménagement	move 145	droit	right 146	garçon	boy 147	vieux	old 148	trop	too 149	même	same 150	elle	she 151	tous	all 152	là	there 153	quand	when 154	jusqu’à	up 155	utiliser	use 156	votre	your 157	manière	way 158	sur	about 159	beaucoup	many 160	puis	then 161	les	them 162	écrire	write 163	voudrais	would 164	comme	like 165	si	so 166	ces	these 167	son	her 168	long	long 169	faire	make 170	chose	thing 171 voir see 172 lui him 173 deux	two 174	a	has 175	regarder	look 176	plus	more 177	jour	day 178	pourrait	could 179	aller	go 180	venir	come 181	fait	did 182	nombre	number 183	son	sound 184	aucun	no 185	plus	most 186	personnes	people 187	ma	my 188	sur	over 189	savoir	know 190	eau	water 191	que	than 192	appel	call 193	première	first 194	qui	who 195	peut	may 196	vers_le_bas	down 197	côté	side 198	été	been 199	maintenant	now 200	trouver	find 201	tête	head 202	supporter	stand 203	propre	own 204	page	page 205	devrait	should 206	pays	country 207	trouvé	found 208	réponse	answer 209	école	school 210	croître	grow 211	étude	study 212	encore	still 213	apprendre	learn 214	usine	plant 215	couvercle	cover 216	nourriture	food 217	soleil	sun 218	quatre	four 219	entre	between 220	état	state 221	garder	keep 222	œil	eye 223	jamais	never 224	dernier	last 225	laisser	let 226	pensée	thought 227	ville	city 228	arbre	tree 229	traverser	cross 230	ferme	farm 231	dur	hard 232	début	start 233	puissance	might 234	histoire	story 235	scie	saw 236	loin	far 237	mer	sea 238	tirer	draw 239	gauche	left 240	tard	late 241	courir	run 242	needs_a_context	don’t 243	tandis_que	while 244	presse	press 245	proche	close 246	nuit	night 247	réel	real 248	vie	life 249	peu	few 250	nord	north 251	livre	book 252	porter	carry 253	a_pris	took 254	science	science 255	manger	eat 256	chambre	room 257	ami	friend 258	a_commencé	began 259	idée	idea 260	poisson	fish 261	montagne	mountain 262	Arrêtez	stop 263	une_fois	once 264	base	base 265	entendre	hear 266	cheval	horse 267	coupe	cut 268	sûr	sure 269	regarder	watch 270	couleur	color 271	face	face 272	bois	wood 273	principal	main 274	ouvert	open 275	paraître	seem 276	ensemble	together 277	suivant	next 278	blanc	white 279	enfants	children 280	commencer	begin 281	eu	got 282	marcher	walk 283	exemple	example 284	facilité	ease 285	papier	paper 286	groupe	group 287	toujours	always 288	musique	music 289	ceux	those 290	tous_les_deux	both 291	marque	mark 292	souvent	often 293	lettre	letter 294	jusqu’à_ce_que	until 295	mile	mile 296	rivière	river 297	voiture	car 298	pieds	feet 299	soins	care 300	deuxième	second 301	assez	enough 302	plaine	plain 303	fille	girl 304	habituel	usual 305	jeune	young 306	prêt	ready 307	au-dessus	above 308	jamais	ever 309	rouge	red 310	liste	list 311	bien_que	though 312	sentir	feel 313	parler	talk 314	oiseau	bird 315	bientôt	soon 316	corps	body 317	chien	dog 318	famille	family 319	direct	direct 320	pose	pose 321	laisser	leave 322	chanson	song 323	mesurer	measure 324	porte	door 325	produit	product 326	noir	black 327	court	short 328	chiffre	numeral 329	classe	class 330	vent	wind 331	question	question 332	arriver	happen 333	complète	complete 334	navire	ship 335	zone	area 336	moitié	half 337	rock	rock 338	ordre	order 339	feu	fire 340	sud	south 341	problème	problem 342	pièce	piece 343	dit	told 344	savait	knew 345	passer	pass 346	depuis	since 347	haut	top 348	ensemble	whole 349	roi	king 350	rue	street 351	pouce	inch 352	multiplier	multiply 353	rien	nothing 354	cours	course 355	rester	stay 356	roue	wheel 357	plein	full 358	force	force 359	bleu	blue 360	objet	object 361	décider	decide 362	surface	surface 363	profond	deep 364	lune	moon 365	île	island 366	pied	foot 367	système	system 368	occupé	busy 369	test	test 370	record	record 371	bateau	boat 372	commun	common 373	or	gold 374	possible	possible 375	plan	plane 376	place	stead 377	sec	dry 378	se_demander	wonder 379	rire	laugh 380	mille	thousand 381	il_ya	ago 382	ran	ran 383	vérifier	check 384	jeu	game 385	forme	shape 386	assimiler	equate 387	chaud	hot 388	manquer	miss 389	apporté	brought 390	chaleur	heat 391	neige	snow 392	pneu	tire 393	apporter	bring 394	oui	yes 395	lointain	distant 396	remplir	fill 397	est	east 398	peindre	paint 399	langue	language 400	entre	among 401	unité	unit 402	puissance	power 403	ville	town 404	fin	fine 405	certain	certain 406	voler	fly 407	tomber	fall 408	conduire	lead 409	cri	cry 410	sombre	dark 411	machine	machine 412	Note	note 413	patienter	wait 414	plan	plan 415	figure	figure 416	étoile	star 417	boîte	box 418	nom	noun 419	domaine	field 420	reste	rest 421	correct	correct 422	capable	able 423	livre	pound 424	Terminé	done 425	beauté	beauty 426	entraînement	drive 427	résisté	stood 428	contenir	contain 429	avant	front 430	enseigner	teach 431	semaine	week 432	finale	final 433	donné	gave 434	vert	green 435	oh	oh 436	rapide	quick 437	développer	develop 438	océan	ocean 439	chaud	warm 440	gratuit	free 441	minute	minute 442	fort	strong 443	spécial	special 444	esprit	mind 445	derrière	behind 446	clair	clear 447	queue	tail 448	produire	produce 449	fait	fact 450	espace	space 451	entendu	heard 452	meilleur	best 453	heure	hour 454	mieux	better 455	vrai	true 456	pendant	during 457	cent	hundred 458	cinq	five 459	rappeler	remember 460	étape	step 461	tôt	early 462	tenir	hold 463	ouest	west 464	sol	ground 465	intérêt	interest 466	atteindre	reach 467	rapide	fast 468	verbe	verb 469	chanter	sing 470	écouter	listen 471	six	six 472	table	table 473	Voyage	travel 474	moins	less 475	matin	morning 476	dix	ten 477	simple	simple 478	plusieurs	several 479	voyelle	vowel 480	vers	toward 481	guerre	war 482	poser	lay 483	contre	against 484	modèle	pattern 485	lent	slow 486	centre	center 487	amour	love 488	personne	person 489	argent	money 490	servir	serve 491	apparaître	appear 492	route	road 493	carte	map 494	pluie	rain 495	règle	rule 496	gouverner	govern 497	tirer	pull 498	froid	cold 499	avis	notice 500	voix	voice"
    lang="fr"
    cards = filter.filter_text(text)
    deck = anki.get_deck('French 500')

    if not filter.check_cards(cards):
        print("ERROR: one or more cards is formatted incorrectly!")
        return
    
    print("Creating deck...")

    for card in cards:
        progress = (int(card["number"]) / len(cards)) * 100

        if(progress % 5 == 0):
            print(f'Progress: {int(progress)}%...')
        anki.add_card(deck, card, lang)

    anki.export_deck(deck, "test_deck")
    print("Finished!")

if __name__ == "__main__":
    main()