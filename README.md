Premier league predictor
Gard Molegoda, Markus Gjerde: 10.11.2024
SCOPE
1. Forretningsmål
Hovedmålet med Premier League Predictor er å lage et verktøy som forutsier utfallet av Premier League-kamper. Verktøyet vil gi verdifull innsikt for sportsanalytikere, spillselskaper og fotballentusiaster. Ved å forutsi kampresultater med god nøyaktighet, kan modellen bidra til bedre beslutninger, økt brukerengasjement og fungere som en ressurs for dem som er interessert i sportsstatistikk. Modellen kan også utvides til bruk for spillselskaper, hvor presise prediksjoner kan påvirke inntekter og kundelojalitet.
2. Bruk og Eksisterende Løsninger
Modellen skal forutsi kampresultater i Premier League, inkludert sannsynlighet for hjemmeseier, uavgjort og borteseier.
Eksisterende løsninger: Dagens metoder omfatter betting-markeder og statistiske modeller brukt av sportsanalytikere.
Manuell tilnærming: Uten maskinlæring baseres prediksjoner på menneskelige analyser ved bruk av enkel statistikk og subjektive vurderinger, noe som er tidkrevende og mindre presist.
3. Forretningsmetrikker
Ytelse vil måles gjennom:
Prediksjonsnøyaktighet: Andelen korrekte prediksjoner basert på historiske data.
Kalibrering: Måling av hvor tett prediksjonssannsynligheter stemmer overens med faktiske utfall.
Engasjement: Målt via brukertid og antall prediksjoner per bruker.
Økonomisk effekt: For kommersielle brukere kan økt nøyaktighet korreleres med inntekt eller brukerengasjement.
4. Systemkomponenter og Pipeline
Premier League Predictor vil bestå av følgende:
Datapipeline: Innsamling og preprosessering av sanntids kampdata og lagstatistikk.
Feature Engineering: Transformering av rådata til relevante egenskaper for modellen.
Modell-inferens: Prediksjonsberegning på prosesserte data.
Postprosessering: Formatering av utdata som lesbare sannsynligheter.
Frontend visning: Presentasjon av prediksjoner via en app eller nettside.
Endringspåvirkning: Endringer i datastrømmer (f.eks. API-oppdateringer) kan påvirke preprosessering og modellens nøyaktighet, noe som kan kreve retrening og tilpasning.

Business Metric for suksess
1.	Treffsikkerhet (Accuracy): Minimum 70% korrekt prediksjon for kampresultater.
2.	Engasjement: Økt brukerinteraksjon (f.eks. antall prediksjoner).
   Maskinlærings- og Software-metrikker
o	Treffsikkerhet (Accuracy): Andel riktige prediksjoner (hjemmeseier, uavgjort, borteseier).
o	Mean Squared Error (MSE): Vist ved forskjellen mellom prediksjoner og faktiske resultater.
o	Precision, Recall, F1-score: For å evaluere modellens presisjon for hver resultatkategori.
Sammenheng med business objective
•	Treffsikkerhet: Høy treffsikkerhet gir pålitelige resultater og øker brukernes tillit og engasjement.
•	MSE: Lav MSE viser at modellen er nøyaktig, noe som øker dens verdi.
•	Latency og Throughput: Lav latency og høy throughput gir en rask og god brukeropplevelse, som fremmer engasjement.
DATA
Datakilder og Type Data:
o	Data: Premier League kampresultater, lagstatistikk, mål, hjemmelag, bortelag, og annen relevant informasjon.
o	Labels: Kampresultat (hjemmeseier, uavgjort, borteseier).
o	Datainnsamling: Data kan hentes fra API-er, sportsdatabaser eller Kaggle-datasett.
Tilgjengelig og Nødvendig Data:
o	Tilgjengelig data: Det finnes historikk for flere sesonger av Premier League.
o	Estimert behov: Minst 5 sesonger, ca. 1900 kamper, for nøyaktige prediksjoner.
Supervised Learning og Labels:
o	Dataene er merket med resultatet av hver kamp (label). Dette brukes til å trene modellen.
o	For å sikre konsistens i labels, hentes data fra pålitelige kilder.
Personvernhensyn og Etikk:
o	Personvern: Ingen personlige data brukes, bare informasjon om lag og kamper.
o	Etikk: Ingen etiske problemer, da det kun handler om sportsprediksjoner.
Datarepresentasjon og Preprosessering
Datarepresentasjon:
o	Dataene vil bli omgjort til tall, med variabler som mål, form og lagets statistikk.
Rensing og Feature Engineering:
o	Rensing: Fjerne feil eller manglende data.
o	Feature Engineering: Lage nye funksjoner som måldifferanse eller lagform.
o	Skalering: Justere tallene slik at de er på samme skala for modellen.

MODELLERING
I å med at dette er et prosjekt som er basert på statistikk vil resultatet kunne bli veldig annerledes enn det som blir predikert. Det har derfor blitt en vanskelig prosess å finne ut om den faktisk funker eller om modellen er dårlig. Det blir mye synsing og meninger som vil være objektive for prosjektet. Et vanskelig prosjekt
DEPLOYMENT
Det er til nå ingen plan om videre drift av prosjektet, men planen er å bruke det til å faktiske teste om resultatene fungerer. Derfor skal dette bli testet i sammenheng med oddstipping som et hobbyprosjekt, én slags finale test for modellen.


REFERANSER
1.	(Inspirasjon for første iterasjon) https://www.kaggle.com/datasets/evangower/premier-league-matches-19922022
2.	(Hentet dataset) https://www.kaggle.com/datasets/saife245/english-premier-league
3.	https://github.com/tara-nguyen/english-premier-league-datasets-for-10-seasons/blob/main/epldat10seasons/epl-allseasons-matchstats.csv



Link til videodemo av prosjektet:
https://youtu.be/90Gna-qPsqY
