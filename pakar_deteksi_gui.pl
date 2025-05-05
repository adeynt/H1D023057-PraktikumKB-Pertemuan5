% DETEKSI JENIS KULIT WAJAH

:-dynamic ciri_pos/1.
:-dynamic ciri_neg/1.

jenis_kulit("Kulit Normal").
jenis_kulit("Kulit Kering").
jenis_kulit("Kulit Berminyak").
jenis_kulit("Kulit Kombinasi").
jenis_kulit("Kulit Sensitif").

ciri(komedo, "Kulit Normal").
ciri(pori_halus, "Kulit Normal").
ciri(komedo, "Kulit Kering").
ciri(pori_halus, "Kulit Kering").
ciri(terkelupas, "Kulit Kering").
ciri(gatal, "Kulit Kering").
ciri(jerawat, "Kulit Kering").
ciri(komedo, "Kulit Berminyak").
ciri(berminyak_all, "Kulit Berminyak").
ciri(jerawat, "Kulit Berminyak").
ciri(gatal, "Kulit Berminyak").
ciri(pori_besar, "Kulit Berminyak").
ciri(komedo, "Kulit Kombinasi").
ciri(berminta_tzone, "Kulit Kombinasi").
ciri(jerawat, "Kulit Kombinasi").
ciri(gatal, "Kulit Kombinasi").
ciri(pori_besar, "Kulit Kombinasi").
ciri(komedo, "Kulit Sensitif").
ciri(jerawat, "Kulit Sensitif").
ciri(urat_tampak, "Kulit Sensitif").
ciri(terkelupas, "Kulit Sensitif").
ciri(gatal, "Kulit Sensitif").

pertanyaan(komedo, Y) :-
    Y = "Apakah Anda memiliki komedo di wajah?".
pertanyaan(berminyak_all, Y) :-
    Y = "Apakah wajah Anda terlihat berminyak di seluruh bagian?".
pertanyaan(berminta_tzone, Y) :-
    Y = "Apakah wajah Anda hanya berminyak di area T-zone (dahi, hidung, dagu)?".
pertanyaan(jerawat, Y) :-
    Y = "Apakah Anda memiliki jerawat di wajah Anda?".
pertanyaan(urat_tampak, Y) :-
    Y = "Apakah urat nadi Anda tampak jelas di area wajah?".
pertanyaan(terkelupas, Y) :-
    Y = "Apakah kulit wajah Anda mudah mengelupas?".
pertanyaan(gatal, Y) :-
    Y = "Apakah Anda sering merasa gatal di area wajah?".
pertanyaan(pori_halus, Y) :-
    Y = "Apakah pori-pori wajah Anda tampak kecil atau halus?".
pertanyaan(pori_besar, Y) :-
    Y = "Apakah pori-pori wajah Anda tampak besar dan terbuka?".

terdeteksi(Jenis) :-
    jenis_kulit(Jenis),
    forall(ciri(Ciri, Jenis), ciri_pos(Ciri)).
