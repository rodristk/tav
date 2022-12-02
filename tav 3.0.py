#Rodrigo Freire dos Santos Alencar

import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb

#pip install pipwin
#pip install PyAudio
# Languages = https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-
#pip install wikipedia

engine = pyttsx3.init()



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S") #for 12 hour clock
    speak("Hora atual")
    speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("Data atual")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Bem vindo de volta Rodrigo")
    time_()
    date_()

    #Greetings

    hour = datetime.datetime.now().hour

    if hour >=6 and hour<12:
        speak("Bom dia para você!")
    elif hour>=12 and hour<18:
        speak("Boa tarde para você!")
    elif hour>=18 and hour<24:
        speak("Boa noite para você!")
    else:
        speak("Tenha uma boa noite!")

    speak("Tavh ao seu serviço. Por favor, me diga como posso ajudar hoje? ")



def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconhecendo.....")
        #query = r.recognize_google(audio,language='en-US')
        query = r.recognize_google(audio,language='pt-BR')
        print(query)

    except Exception as e:
        print(e)
        print("Pode repetir, por favor.....")
        return "Nenhum"
    return query

TakeCommand()


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    #for this function, you mist enable low security in you gmail which you are going to use as sender
    server.login('username@gmail.com','password')
    server.sendmail('username@gmail.com',to,content)
    server.close()

def wikipedia_():
    speak("Pesquisando....")
    #buscar=input("Oque devo pesquisar?")
    query==query.replace('wikipédia','')
    result=wikipedia.summary(query,sentences=3)
    speak('De acordo com a wikipédia')
    print(result)
    speak(result)

#if _name_ == "_main_":
if __name__ == "__main__":

    wishme()

    while True:
        query = TakeCommand().lower()

        #All commands will be stored in lower case in query
        #For easy recognition

        if 'hora' in query: # tell us time when asked
            time_()

        elif 'data' in query: # tell us date when asked
            date_()

        elif 'wikipédia' or 'wikipedia' or 'pesquisar' in query:
            wikipedia_()
 
#Funções Teológicas do Sistema 

        elif 'mandamentos' in query:            
            mandamentos=["1 Não terás outros deuses diante de mim",
                         "2 Não farás para ti imagem de escultura, não as adorarás",
                         "3 Não tomarás o nome do Senhor em vão",
                         "4 Lembra-te do dia de Sábado para o santificar",
                         "5 Honrar pai e mãe",
                         "6 Não matarás",
                         "7 Não adulterarás",
                         "8 Não furtarás",
                         "9 Não dirás falso testemunho",
                         "10 Não cobiçarás",
                         "Fonte: Exôdo 20"]
            print(mandamentos)
            speak(mandamentos)     

        elif 'criação' in query:            
            criacao=["Primeiro dia, Deus separou a luz das trevas",
                     "Segundo dia, Deus separou o céu das águas",
                     "Terceiro dia, Deus separou a Terra das águas e criou as plantas",
                     "Quarto dia, Deus criou o sol a lua e as estrelas",
                     "Quinto dia, Deus criou as criaturas aquáticas e os pássaros",
                     "Sexto dia, Deus criou as criaturas da terra e os seres humanos",
                     "Abençoou Deus o sétimo dia, e o santificou; porque nele descansou de toda a sua obra",
                     "Fonte: Gênesis 1 e 2"]
            print(criacao)
            speak(criacao)         
            
        elif 'pentateuco' in query: 
            pentateuco=["gênesis",
                        "êxodo",
                        "levítico",
                        "números",
                        "deuteronômio"]
            print(pentateuco)
            speak(pentateuco)

        elif 'históricos antigos' in query: 
            historicos_at=["josué",
                        "juízes",
                        "rute",
                        "1 samuel",
                        "2 samuel",
                        "1 reis",
                        "2 reis",
                        "1 crônicas",
                        "2 crônicas",
                        "esdras",
                        "neemias",
                        "ester"]
            print(historicos_at)
            speak(historicos_at)

        elif 'poéticos' in query: 
            poeticos=["jó",
                      "salmos",
                      "provérbios",
                      "eclesiastes",
                      "cantares"]
            print(poeticos)
            speak(poeticos)

        elif 'profetas maiores' in query: 
            profetas_maiores=["isaías",
                              "jeremias",
                              "lamentações",
                              "ezequiel",
                              "daniel"]
            print(profetas_maiores)
            speak(profetas_maiores)

        elif 'profetas menores' in query:                       
            profetas_menores=["oséias",
                              "joel",
                              "amós",
                              "obadias",
                              "Jonas",
                              "Miquéias",
                              "Naum",
                              "Habacuque",
                              "Sofonias",
                              "Ageu",
                              "Zacarias",
                              "Malaquias"]
            print(profetas_menores)
            speak(profetas_menores)

        elif 'antigo testamento' in query: 
            antigo_testamento=[pentateuco,historicos_at,poeticos,profetas_maiores,profetas_menores]
            print(antigo_testamento)
            speak(antigo_testamento)

        elif 'novo testamento' in query: 
            novo_testamento=[evangelhos,historico_nt,epistolas_paulinas,epistolas_gerais,profetico]
            print(novo_testamento)
            speak(novo_testamento)

        elif 'evangelhos' in query: 
            evangelhos=["mateus",
                        "marcos",
                        "lucas",
                        "joão"]
            print(evangelhos)
            speak(evangelhos)

        elif 'históricos novos' in query: 
            historico_nt=["atos dos apóstolos"]
            print(historico_nt)
            speak(historico_nt)

        elif 'espistolas paulinas' in query: 
            epistolas_paulinas=["romanos",
                                "1 coríntios",
                                "2 coríntios",
                                "gálatas",
                                "efésios",
                                "filipenses",
                                "colossenses",
                                "1 tessalonicenses",
                                "2 tessalonicenses",
                                "1 timóteo",
                                "2 timóteo",
                                "tito",
                                "filemom",
                                "hebreus"]
            print(epistolas_paulinas)
            speak(epistolas_paulinas)

        elif 'espistolas gerais' in query: 
            epistolas_gerais=["tiago",
                            "1 pedro",
                            "2 pedro",
                            "1 joão",
                            "2 joão",
                            "3 joão",
                            "judas"]
            print(epistolas_gerais)
            speak(epistolas_gerais)

        elif 'profético' in query: 
            profetico=["apocalipse"]
            print(profetico)
            speak(profetico)
         
        elif 'livros da bíblia' in query:
            livros_biblia=[antigo_testamento,novo_testamento]
            print("39 no antigo testamento, 27 no novo testamento são:",livros_biblia)
            speak("39 no antigo testamento, 27 no novo testamento são:",livros_biblia)

        elif 'divisão literária' in query:
            divisao_literaria=["pentatuco","poéticos","evangelhos","históricos","epistolas","profeticos"]
            print(divisao_literaria)
            speak(divisao_literaria)

        elif 'alfabeto grego' in query:
            alfabeto_grego=["α Αlfa","β Beta","γ Gama","δ Delta","ε Épsilon",
            "ζ Zeta","η Eta","θ Teta","ι Iota","κ Capa","λ Lambda","μ Mi",
            "ν Ni","ξ Csi","ο Ómicron","π Pi","ρ Rô","σ Sigma","τ Tau","υ Úpsilon",
            "φ Fi","χ Qui","ψ Psi","ω Ômega","ϝ Digama","ͱ Hetá","ϻ San","ϸ Sho",
            "ϛ Stigma","ϙ Qoppa","ͳ Sampi"]   
            print(alfabeto_grego)
            speak(alfabeto_grego)

        elif 'alfabeto hebraico' in query:
            alfabeto_hebraico=["א Alef","בּ Bet","ג Guímel","ד Dalet","ה He",
            "ו Vav","ז Zayin","ח Het","ט Tet","י Yod","כּ kaf","ך Kaf final","ל Lamed",
            "מ Mem","ם Mem final","נ Nun","ן Nun final","ס Samek","ע Ayin","פּ Pe",
            "ף Pe final","צ Tsadi","ץ Tsade final","ק Qof","ר Resh","ש Shin","תּ Tav"]   
            print(alfabeto_hebraico)
            speak(alfabeto_hebraico)
            
        elif 'alfabeto aramaico' in query:
            alfabeto_aramaico=["𐡀 Ālaph","𐡁 Bēth","𐡂 Gāmal","𐡃 Dālath","𐡄 Hē",
            "𐡅 Waw","𐡆 Zain","𐡇 Ḥēth","𐡈 Ṭēth","𐡉 Yudh","𐡊 Kāph","𐡋 Lāmadh","𐡌 Mim",
            "𐡍 Nun","𐡎 Semkath","𐡏 Ayin","𐡐 Pē","𐡑 Ṣādhē","𐡒 Qoph",
            "𐡓 Rēsh","𐡔 Shin","𐡕 Tau"]   
            print(alfabeto_aramaico)
            speak(alfabeto_aramaico)

        elif 'alfabeto latino' in query:
            alfabeto_latino=["a Á","b Bê","c Cê","d Dê","e É",
            "f Éfe","g Gê","h Agá","i I","j Jóta","k Kapa","l Éle",
            "m Éme","n Éne","o Ó","p Pê","q Quê","r Érre","s Ésse","t Tê",
            "u U","v Vê","w Dabliu","x Xis","y Ípsilon","z Zê"]   
            print(alfabeto_latino)
            speak(alfabeto_latino)       
    
        elif 'léxico 08372' or "ta’ e" in query:
            lexico_08372=["תא 08372 ta’ e .1) câmara, sala da guarda"]
            print(lexico_08372)
            speak(lexico_08372)

        elif 'léxico 08373' or "ta’ab" in query:
            lexico_08373=["תאב 08373 ta’ab .1) (Qal) anelar"]
            print(lexico_08373)
            speak(lexico_08373)

        elif 'léxico 08374' or "ta’ab" in query:
            lexico_08374=["תאב תאב 08374 ta’ab .1) (Piel) detestar, abominar"]
            print(lexico_08374)
            speak(lexico_08374)

        elif 'léxico 08375' or "ta’abah" in query:
            lexico_08375=["תאבה 08375 ta’abah .1) anelo"]
            print(lexico_08375)
            speak(lexico_08375)

        elif 'léxico 08376' or "ta’ah" in query:
            lexico_08376=["תאה 08376 ta’ah .1) (Piel) marcar, assinalar"]
            print(lexico_08376)
            speak(lexico_08376)

        elif 'léxico 08377' or "tow" in query:
            lexico_08377=["תאו 08377 t e’ow e תוא tow’ (a forma original) .1) boi selvagem, antílope, oryx. 1a) talvez um animal extinto, o significado exato é incerto"]
            print(lexico_08377)
            speak(lexico_08377)

        elif 'léxico 08378' or "ta’avah" in query:
            lexico_08378=["תאוה 08378 ta’avah .1) desejo 1a) desejo, vontade, anseios do coração de alguém 1a1) cobiça, apetite, concupiscência (no mau sentido) 1b) coisa desejada, objeto de desejo"]
            print(lexico_08378)
            speak(lexico_08378)

        elif 'léxico 08379' or "ta’avah" in query:
            lexico_08379=["08379 תאוה ta’avah .1) fronteira, limite 1a) significado incerto"]
            print(lexico_08379)
            speak(lexico_08379)

        elif 'léxico 08380' or "ta’om" in query:
            lexico_08380=["תאום 08380 ta’owm ou תאם ta’om .1) gêmeo"]
            print(lexico_08380)
            speak(lexico_08380)

        elif 'léxico 08381' or "ta’alah" in query:
            lexico_08381=["תאלה 08381 ta’alah .1) maldição"]
            print(lexico_08381)
            speak(lexico_08381)

        elif 'léxico 08382' or "ta’am" in query:
            lexico_08382=["תאם 08382 ta’am .1) ser duplo, ser unido 1a) (Qal) ser duplo 1b) (Hifil) dar à luz gêmeos"]
            print(lexico_08382)
            speak(lexico_08382)

        elif 'léxico 08383' or "t e’un" in query:
            lexico_08383=["תאן 08383 t e’un ou (plural) .1) labuta"]
            print(lexico_08383)
            speak(lexico_08383)
        
        elif 'léxico 08384' or "t e’en" in query:
            lexico_08384=["תאן 08384 t e’en ou (no sing., fem.) תאנה t e’enah .1) figo, figueira"]
            print(lexico_08384)
            speak(lexico_08384)

        elif 'léxico 08385' or "ta’anah" in query:
            lexico_08385=["תאנה 08385 ta’anah ou תאנה to’anah .1) ocasião, tempo do cio ou de copulação, impulso sexual (referindo-se aos animais) 2) ocasião, oportunidade (para uma discussão)"]
            print(lexico_08385)
            speak(lexico_08385)

        elif 'léxico 08386' or "ta’aniyah" in query:
            lexico_08386=["תאניה 08386 ta’aniyah .1) luto, lamentação"]
            print(lexico_08386)
            speak(lexico_08386)

        elif 'léxico 08387' or "Ta’anath Shiloh" in query:
            lexico_08387=["תאנת שלה 08387 Ta’anath Shiloh .Taanate-Siló = 'acesso a Siló' 1) um marco na divisa de Efraim"]
            print(lexico_08387)
            speak(lexico_08387)

        elif 'léxico 08388' or "ta’ar" in query:
            lexico_08388=["תאר 08388 ta’ar .1) (Qal) ser esboçado, inclinar, delinear, estender 1a) significado incerto 2) (Piel) esboçar, fazer um traçado"]
            print(lexico_08388)
            speak(lexico_08388)

        elif 'léxico 08389' or "to’ar" in query:
            lexico_08389=["08389 תאר to’ar .1) molde, forma, esboço, figura, aspecto"]
            print(lexico_08389)
            speak(lexico_08389)

        elif 'léxico 08390' or "Ta’area" in query:
            lexico_08390=["0839תארע 0 Ta’area Taréia = 'câmara de um vizinho'.1) um benjamita, filho de Mica da família de Saul"]
            print(lexico_08390)
            speak(lexico_08390)

        elif 'léxico 08391' or "te’ashshuwr" in query:
            lexico_08391=["0839תאשור1 t e’ashshuwr .1) um tipo de árvore 1a) buxo - um árvore pequena sempre verde 1b) talvez cipreste ou cedro"]
            print(lexico_08391)
            speak(lexico_08391)

        elif 'léxico 08392' or "tebah" in query:
            lexico_08392=["0839תבה 2 tebah . 1) arca 1a) embarcação que Noé construiu 1b) cesta em que Moisés foi colocado"]
            print(lexico_08392)
            speak(lexico_08392)

        elif 'léxico 08393' or "tebuw’ah" in query:
            lexico_08393=["0839תבואה 3 t ebuw’ah . 1) produção, produto, renda 1a) produto, produção, safra (produtos agrícolas, geralmente) 1b) renda, rendimentos 1c) ganho (referindo-se a sabedoria) (fig.) 1d) fruto dos lábios (fig.)"]
            print(lexico_08393)
            speak(lexico_08393)

        elif 'léxico 08394' or "tabuwn" in query:
            lexico_08394=["0839תבון 4 tabuwn e (fem.) תבונה t ebuwnah ou תובנה towbunah . 1) compreensão, inteligência 1a) o ato do entendimento 1a1) habilidade 1b) a capacidade do entendimento 1b1) inteligência, compreensão, percepção 1c) o objeto do conhecimento 1d) professor (personificação)"]
            print(lexico_08394)
            speak(lexico_08394)

        elif 'léxico 08395' or "tebuwcah" in query:
            lexico_08395=["0839תבוסה 5 tebuwcah . 1) o calcar aos pés, opressão, ruína, queda, destruição"]
            print(lexico_08395)
            speak(lexico_08395)

        elif 'léxico 08396' or "Tabowr" in query:
            lexico_08396=["0839תבור 6 Tabowr  = “colina” n. pr. monte. 1) um monte na planície de Esdrelom que que ergue-se abruptamente e de forma isolada exceto por uma estreita cordilheira no lado ocidental que a conecta aos montes de Nazaré n. pr. loc. 2) uma cidade próxima ao cimo do monte Tabor (1) 3) uma cidade de levites meraritas localizada no território de Zebulom n. pr. de árvore 4) local de um carvalho que se encontrava no caminho de Saul ao voltar para casa depois de ter sido ungido por Samuel"]
            print(lexico_08396)
            speak(lexico_08396)

        elif 'léxico 08397' or "tebel" in query:
            lexico_08397=["0839תבל 7 tebel . 1) confusão (violação da natureza ou da ordem divina) 1a) perversão (pecado sexual)"]
            print(lexico_08397)
            speak(lexico_08397)

        elif 'léxico 08398' or "tebel" in query:
            lexico_08398=["0839תבל 8 tebel . 1) mundo"]
            print(lexico_08398)
            speak(lexico_08398)

        elif 'léxico 08399' or "tabliyth" in query:
            lexico_08399=["08399 תבלית tabliyth . 1) destruição"]
            print(lexico_08399)
            speak(lexico_08399)

        elif 'léxico 08400' or "teballul" in query:
            lexico_08400=["תבלל 08400 teballul . 1) obscuridade, defeito (na visão), confusão"]
            print(lexico_08400)
            speak(lexico_08400)

        elif 'léxico 08401' or "teben" in query:
            lexico_08401=["תבן 08401 teben . 1) palha, restolho 1a) como material de construção 1b) como forragem para o gado"]
            print(lexico_08401)
            speak(lexico_08401)

        elif 'léxico 08402' or "Tibni" in query:
            lexico_08402=["תבני 08402 Tibni . Tibni = “inteligente” 1) aspirante ao trono do reino do norte, de Israel, depois da morte de Zimri; lutou por 4 anos com a facção rival cujo líder era Omri; morreu depois de 4 anos deixando o trono para Omri"]
            print(lexico_08402)
            speak(lexico_08402)

        elif 'léxico 08403' or "tabniyth" in query:
            lexico_08403=["08403 תבנית tabniyth.1) modelo, planta, forma, construção, figura 1a) construção, estrutura 1a1) sentido duvidoso 1b) modelo 1c) figura, imagem (referindo-se aos ídolos)"]
            print(lexico_08403)
            speak(lexico_08403)
        
        elif 'léxico 08404' or "Tab erah" in query:
            lexico_08404=["08404 תבערה Tab erah .Taberá = “labareda” 1) um lugar no deserto de Parã "]
            print(lexico_08404)
            speak(lexico_08404)
     
        elif 'léxico 08405' or "Tebets" in query:
            lexico_08405=["08405 תבץ Tebets.Tebes = “ilustre” 1) uma vila próxima a Siquém "]
            print(lexico_08405)
            speak(lexico_08405)
        
        elif 'léxico 08406' or "tebar" in query:
            lexico_08406=["08406 תבר tebar ̂ (aramaico).1) quebrar 1a) (Peal) quebrado em pedaços (particípio)"]
            print(lexico_08406)
            speak(lexico_08406)
         
        elif 'léxico 08407' or "Tiglath Pil’ecer" in query:
            lexico_08407=["08407 פלאסר תגלת Tiglath Pil’ecer ou פלסר תגלת Tiglath P elecer ̂ ou פלנאסר תלגת Tilgath Piln e’ecer ̂ ou פלנסר תלגת Tilgath Pilnecer.Tiglate-Pileser ou Tiglate-Pilneser = “tu descobrirás o prodigioso vínculo” 1) um rei assírio que atacou Samaria ou o reino do Norte (Israel) no reinado de Peca"]
            print(lexico_08407)
            speak(lexico_08407)

        elif 'léxico 08408' or "tagmuwl" in query:
            lexico_08408=["08408 תגמול tagmuwl.1) benefício, ato de graça"]
            print(lexico_08408)
            speak(lexico_08408)
        
        elif 'léxico 08409' or "tigrah" in query:
            lexico_08409=["08409 תגרה tigrah.1) contenda, luta, conflito, hostilidade "]
            print(lexico_08409)
            speak(lexico_08409)
        
        elif 'léxico 08410' or "tidhar" in query:
            lexico_08410=["08410 תדהר tidhar.1) uma espécie de árvore de madeira de lei 1a) talvez buxo, olmeiro "]
            print(lexico_08410)
            speak(lexico_08410)
        
        elif 'léxico 08411' or "tediyra’" in query:
            lexico_08411=["08411 תדירא tediyra’ ̂ (aramaico).1) continuação, continuidade, perpetuity 1a) constantemente (como advérbio) "]
            print(lexico_08411)
            speak(lexico_08411)
        
        elif 'léxico 08412' or "Tadmor" in query:
            lexico_08412=["08412 תדמר Tadmor ou תמר Tammor (1Rs 9.18).Tadmor = “palmeira” 1) uma cidade construída por Salomão depois de ter conquistado Hamate-Zoba "]
            print(lexico_08412)
            speak(lexico_08412)
        
        elif 'léxico 08413' or "Tid al" in query:
            lexico_08413=["08413 תדעל Tid al.Tidal = “grande filho” 1) líder de varias tribos nômades e um aliado de Quedorlaomer"]
            print(lexico_08413)
            speak(lexico_08413)
        
        elif 'léxico 08414' or "tohuw" in query:
            lexico_08414=[".1) informe, confusão, irrealidade, vazio 1a) sem forma (referindo-se à terra primitiva) 1a1) nada, espaço vazio 1b) o que é vazio ou irreal (referindo-se aos ídolos) (fig.) 1c) desolação, deserto (referindo-se a lugares ermos) 1d) lugar de caos 1e) vaidade"]
            print(lexico_08414)
            speak(lexico_08414)
        
        elif 'léxico 08415' or "tehowm" in query:
            lexico_08415=["08415 תהום t ehowm ̂ ou תהם t ehom.1) profundidade, profundezas, lugares profundos, abismo, o abismo, oceano 1a) profundezas (referindo-se a águas subterrâneas) 1b) profundidade, oceano, profundezas (do oceano) 1c) oceano primevo, abismo 1d) fundura, profundeza (de rio) 1e) abismo, a sepultura"]
            print(lexico_08415)
            speak(lexico_08415)

        elif 'léxico 08416' or "tehillah " in query:
            lexico_08416=["1) louvor, cântico ou hino de louvor 1a) louvor, adoração, ação de graças (rendida a Deus) 1b) ato de louvor geral ou público 1c) cântico de louvor (como título) 1d) louvor (exigido pelas qualidades ou atos ou atributos de Deus) 1e) renome, fama, glória 1e1) de Damasco, de Deus 1e2) objeto de louvor, possuidor de renome (fig.)"]
            print(lexico_08416)
            speak(lexico_08416)
        
        elif 'léxico 08417' or "toholah" in query:
            lexico_08417=["08417 תהלה toholah.1) erro "]
            print(lexico_08417)
            speak(lexico_08417)

        elif 'léxico 08418' or "tahalukah" in query:
            lexico_08418=["08418 תהלכה tahalukah.1) procissão "]
            print(lexico_08418)
            speak(lexico_08418)
        
        elif 'léxico 08419' or "tahpukah" in query:
            lexico_08419=["08419 תהפכה tahpukah.1) perversidade, coisa perversa"]
            print(lexico_08419)
            speak(lexico_08419)

        elif 'léxico 08420' or "tav" in query:
            lexico_08420=["08420 תו tav.1) desejo, marca 1a) marca (como um sinl de dispensa de julgamento)"]
            print(lexico_08420)
            speak(lexico_08420)
        
        elif 'léxico 08421' or "tuwb" in query:
            lexico_08421=["08421 תוב tuwb (aramaico).1) retornar, voltar 1a) (Peal) retornar, voltar 1b) (Afel) 1b1) restituir, devolver, responder 1b2) devolver"]
            print(lexico_08421)
            speak(lexico_08421)
    
        elif 'léxico 08422' or "Tuwbal" in query:
            lexico_08422=["08422 תובל Tuwbal ou תבל Tubal.Tubal = “tu serás trazido” 1) filho de Jafé and neto de Noé n. pr. terr. 2) uma região na parte oriental da Ásia Menor 2a) talvez quase idêntica à Capadócia"]
            print(lexico_08422)
            speak(lexico_08422)
        
        elif 'léxico 08423' or "tebar" in query:
            lexico_08423=["08423 קין תובל Tuwbal Qayin.Tubalcaim = “tu serás trazido de Caim” 1) filho de Lameque com sua esposa Zilá e o primeiro a trabalhar em metal"]
            print(lexico_08423)
            speak(lexico_08423)

        elif 'léxico 08424' or "tuwgah" in query:
            lexico_08424=["08424 תוגה tuwgah.1) lamento, tristeza, pesar"]
            print(lexico_08424)
            speak(lexico_08424)
        
        elif 'léxico 08425' or "Towgarmah" in query:
            lexico_08425=["08425 תוגרמה Towgarmah ou תגרמה Togarmah.Togarma = “tu a quebrarás” n. pr. m. 1) filho de Gômer, neto de Jafé, e bisneto de Noé n. pr. terr. 2) território ocupado pelos descendentes de Togarma 2a) provavelmente a região conhecida como Armênia"]
            print(lexico_08425)
            speak(lexico_08425)

        elif 'léxico 08426' or "towdah" in query:
            lexico_08426=["08426 תודה towdah.1) confissão, louvor, ação de graças 1a) dar louvor a Deus 1b) ação de graças em cânticos de culto litúrgico, hino de louvor 1c) coro ou procissão ou linha ou companhia de ação de graças 1d) oferta de gratidão, sacrifício de ação de graças 1e) confissão"]
            print(lexico_08426)
            speak(lexico_08426)
        
        elif 'léxico 08427' or "tavah" in query:
            lexico_08427=["08427 תוה tavah.1) rabiscar, limitar, marcar, fazer ou colocar uma marca 1a) (Piel) marcar 1b) (Hifil) colocar uma marca"]
            print(lexico_08427)
            speak(lexico_08427)

        elif 'léxico 08428' or "tavah" in query:
            lexico_08428=["תוה 08428 tavah.1) (Hifil) afligir, ferir, aborrecer, causar dor 1a) significado provável"]
            print(lexico_08428)
            speak(lexico_08428)
        
        elif 'léxico 08429' or "tevahh" in query:
            lexico_08429=["08429 תוה tevahh (aramaico). 1) (Peal) estar espantado, estar alarmado"]
            print(lexico_08429)
            speak(lexico_08429)

        elif 'léxico 08430' or "Towach" in query:
            lexico_08430=["תוח 08430 Towach. Toá = “humilde” 1) filho de Zufe, pai de Eliel, and ancestral de Samuel e Hemã"]
            print(lexico_08430)
            speak(lexico_08430)
        
        elif 'léxico 08431' or "towcheleth" in query:
            lexico_08431=["תוחלת 08431 towcheleth. 1) esperança"]
            print(lexico_08431)
            speak(lexico_08431)

        elif 'léxico 08432' or "tavek" in query:
            lexico_08432=["תוך 08432 tavek. 1) meio 1a) meio 1b) para dentro, pelo meio de (depois de verbos de movimento) 1c) entre (referindo-se a um grupo de pessoas) 1d) entre (referindo-se a objetos dispostos em pares) 1e) dentre (quando para tirar, separar, etc.)"]
            print(lexico_08432)
            speak(lexico_08432)
        
        elif 'léxico 08433' or "towkechah" in query:
            lexico_08433=["תוכחה 08433 towkechah e תוכחת towkachath. 1) repreensão, correção, censura, punição, castigo 2) argumento, reprimenda 2a) argumento, contestação 2b) reprimenda, desaprovação 2c) correção, repreensão"]
            print(lexico_08433)
            speak(lexico_08433)

        elif 'léxico 08434' or "Towlad" in query:
            lexico_08434=["תולד 08434 Towlad. Tolade = “geração” 1) um vila em Simeão 1a) também “Eltolade”"]
            print(lexico_08434)
            speak(lexico_08434)

        elif 'léxico 08435' or "towledah" in query:
            lexico_08435=["ולדה ת 08435 towledah ou תלדה tol edah. 1) descendentes, conseqüências, condutas, gerações, genealogias 1a) narrativa acerca de homens e de seus descendentes 1a1) lista genealógica dos descendentes de alguém 1a2) contemporâneos de alguém 1a3) curso da história (referindo-se à crição, etc.) 1b) geração ou relato dos céus (metaf.)"]
            print(lexico_08435)
            speak(lexico_08435)
        
        elif 'léxico 08436' or "Tuwlon" in query:
            lexico_08436=["תולן 08436 Tuwlon. Tilom = “dom” 1) um judaíta, filho de Simão"]
            print(lexico_08436)
            speak(lexico_08436)

        elif 'léxico 08437' or "towlal" in query:
            lexico_08437=["תולל 08437 towlal. 1) opressor, espoliador 1a) significado incerto"]
            print(lexico_08437)
            speak(lexico_08437)

        elif 'léxico 08438' or "towla" in query:
            lexico_08438=["תולע 08438 towla e (fem.) תולעה towle ah ou תולעת towla ath ou תלעת tola ath. 1) verme, tecido escarlate, carmesim 1a) verme - a fêmea “coccus ilicis” 1b) tecido escarlate, carmesim, escarlate 1b1) a tinta feita do corpo seco da fêmea da lagarta “coccus ilicis” 2) verme, larva 2a) verme, lagarta 2b) a lagarta “coccus ilicis”"]
            print(lexico_08438)
            speak(lexico_08438)
        
        elif 'léxico 08439' or "Towla" in query:
            lexico_08439=["08439 תולע Towla. Tola = “verme” 1) o primogênito de Issacar e progenitor da família de Tolaítas 2) um homem de Issacar, filho de Puá e juiz de Israel depois de Abimeleque"]
            print(lexico_08439)
            speak(lexico_08439)

        elif 'léxico 08440' or "Towla ìy" in query:
            lexico_08440=["תולעי 08440 Towla ìy. tolaíta = ver Tola “verme” 1) descendentes de Tola, o filho de Issacar"]
            print(lexico_08440)
            speak(lexico_08440)

        elif 'léxico 08441' or "tow ebah" in query:
            lexico_08441=["תועבה 08441 tow ebah ou תעבה to ebah .1) uma coisa repugnante, abominação, coisa abominável 1a) em sentido ritual (referindo-se ao alimento impuro, ídolos, casamentos mistos) 1b) em sentido ético (referindo-se à impiedade, etc.)"]
            print(lexico_08441)
            speak(lexico_08441)

        elif 'léxico 08442' or "tow ah" in query:
            lexico_08442=["תועה 08442 tow ah . 1) erro, perambulação, impiedade, perversões 1a) erro (em moral e religião) 1b) confusão, distúrbio"]
            print(lexico_08442)
            speak(lexico_08442)

        elif 'léxico 08443' or "tow aphah" in query:
            lexico_08443=["תועפה 08443 tow aphah . 1) eminência, chifres imponentes, cimo 1a) eminência (referindo-se aos chifres altos, picos das montanhas, prata)"]
            print(lexico_08443)
            speak(lexico_08443)

        elif 'léxico 08444' or "towtsa’ah" in query:
            lexico_08444=["תוצאה 08444 towtsa’ah ou תצאה totsa’ah . 1) saída, fronteira, partida, extremidade, fim, origem, fuga 1a) saída, extremo (de uma fronteira) 1b) fonte (da vida) 1c) o escapar (da morte) "]
            print(lexico_08444)
            speak(lexico_08444)

        elif 'léxico 08445' or "Towqahath" in query:
            lexico_08445=["תוקהת 08445 Towqahath . Tocate = “esperança” 1) pai de Salum, o marido da profetiza Hulda na época de Josias, rei de Judá "]
            print(lexico_08445)
            speak(lexico_08445)

        elif 'léxico 08440' or "Towla" in query:
            lexico_08440=[" . "]
            print(lexico_08440)
            speak(lexico_08440)

        elif 'léxico 08446' or "tuwr" in query:
            lexico_08446=["תור 08446 tuwr . 1) procurar, esquadrinhar, espionar, investigar 1a) (Qal) 1a1) procurar, selecionar, descobrir como fazer alguma coisa 1a2) espionar, investigar 1a2a) investigadores, espiões (particípio) 1a3) percorrer 1a3a) mercador, negociante (particípio) 1b) (Hifil) fazer uma investigação, fazer um reconhecimento "]
            print(lexico_08446)
            speak(lexico_08446)

        elif 'léxico 08447' or "tor" in query:
            lexico_08447=["תור 08447 towr ou תר tor . 1) diadema, trança, volta (de cabelo ou ouro) 2) (CLBL) sucessão, ordem "]
            print(lexico_08447)
            speak(lexico_08447)

        elif 'léxico 08448' or "towr" in query:
            lexico_08448=["תור 08448 towr . 1) diadema, trança, volta (de cabelo ou ouro) 2) (CLBL) custume, hábito, modo "]
            print(lexico_08448)
            speak(lexico_08448)

        elif 'léxico 08449' or "tor" in query:
            lexico_08449=["08449 תור towr ou תר tor . 1) pomba, pomba-rola"]
            print(lexico_08449)
            speak(lexico_08449)

        elif 'léxico 08450' or "towr" in query:
            lexico_08450=["תור 08450 towr (aramaico) . 1) touro, novilho (para sacrifício)"]
            print(lexico_08450)
            speak(lexico_08450)

        elif 'léxico 08451' or "torah" in query:
            lexico_08451=["תורה 08451 towrah ou תרה torah . 1) lei, orientação, instrução 1a) instrução, orientação (humana ou divina) 1a1) conjunto de ensino profético 1a2) instrução na era messiânica 1a3) conjunto de orientações ou instruções sacerdotais 1a4) conjunto de orientações legais 1b) lei 1b1) lei da oferta queimada 1b2) referindo-se à lei especial, códigos de lei 1c) costume, hábito 1d) a lei deuteronômica ou mosaica"]
            print(lexico_08451)
            speak(lexico_08451)

        elif 'léxico 08452' or "towrah" in query:
            lexico_08452=["תורה 08452 towrah . 1) costume, hábito, modo, lei (humana) "]
            print(lexico_08452)
            speak(lexico_08452)

#Outras Funções do Sistema            

elif 'escrever email' or 'escrever e-mail' in query:
            try:
                speak("Oque devo fazer?")
                content=TakeCommand()
                #provide reciever email address

                speak("Quem é o receptor?")
                reciever=input("Insira o email do destinatário:")
                to = reciever
                sendEmail(to,content)
                speak(content)
                speak('O email foi enviado.')

            except Exception as e:
                print(e)
                speak("Não foi possível enviar o email.")  

elif 'pesquisar no chrome' in query:
            speak('Oque irei pesquisar?')
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            #chromepath is location of chrome's installation on Computer

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com') #only open websites with '.com' at end.