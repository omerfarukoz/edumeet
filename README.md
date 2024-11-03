# EduMeet

EduMeet, sunumlarınızın baş belası yapay zekayla donatılmış bir meeting platformudur. Sadece insanların bulunduğu platformların aksine EduMeet, sunumlarınızı arkasında Gemini ve diğer Google Cloud Projects ürünlerinin bulunduğu güçlü teknolojiler ile farklı bir boyuta taşıyor. Kullanmak için yapmanız gereken tek şey ise meeting platformu olarak [edumeet.tech](http://edumeet.tech)’i tercih etmek.

## Özellikler

•⁠  ⁠*Yapay Zeka Destekli Karakter*: Meeting esnasında size eşlik eden Gemini destekli karakterimiz, toplantınıza katılıyor, ekran paylaşımınızı izliyor, kameranız ve mikrofonunuz açık ise sizi algılıyor ve anlıyor.
•⁠  ⁠*Yanlış Bilgileri Düzeltme*: Aktardığınız yanlış bilgileri o an sizinle sesli şekilde konuşarak düzeltiyor.
•⁠  ⁠*Etkileşimli Sorular*: Anlattığınız konu üzerinden size sesli şekilde sorular yöneltiyor.
•⁠  ⁠*Yüz İfadesi ve Ses Analizi*: Anlattığınız konunun yanı sıra anlatış biçiminizi ve yüz ifadenizi algılayarak iletişim kuruyor.

## Nasıl Çalışır?

EduMeet, prensipleri çerçevesinde aktarılan bilginin doğruluğuna, sunum yapan bireyin kullandığı materyaller ile anlattıkları arasındaki uyuma ve aktarılan bilginin zenginleştirilmesi için konu üzerinden sorular sormaya özen gösteriyor. Yanıtlar meeting esnasında canlı olacak şekilde sunum yapan bireyin takındığı konuşma biçimi ve yüz ifadesine göre hazırlanıp, yapay zeka karakterimiz vasıtasıyla sesli şekilde iletiliyor.

### İşlem Aşamaları

1.⁠ ⁠*Yüz İfadesinin Algılanması*: Google Vision’un Face Detection özelliği sayesinde verilen görüntüdeki birey algılanıyor ve yüz ifadesinden yorumlanması gereken veriler sağlanıyor. Gelen veriler, Gemini 1.5 Flash vasıtasıyla hızlı bir şekilde yorumlanıp tek bir duygu ifadesine dönüştürülüyor.

2.⁠ ⁠*Ses Verisinin Yorumlanması*: Gemini’ın verilen ses dosyasını algılama özelliği sayesinde ses verisi analiz edilmek için gönderiliyor. Gemini burada konuşan kişinin konuşma şeklini yorumluyor ve anlatılanları analiz ederek konu ve yanlış bilgi taraması yapıyor. Daha sonra konuyu ve yanlış bilgiyi belirtilip soru üretiliyor.

3.⁠ ⁠*Paylaşılan Görüntünün Algılanması*: Elde edilen ekran verileri Google Video Intelligence ve Google Vision kullanılarak Text Detection, Label Detection ve Speech Transcription özellikleri ile ayrıştırılarak algılanıyor. Elde edilen veriler Gemini kullanılarak doğruluğuna, birbirleriyle uyumuna göre analiz ediliyor ve algılanan yanlış bilgi ve uyumsuzlukların sebepleri belirtiliyor, ayrıca soru üretiliyor.

4.⁠ ⁠*Sonuçların Birleştirilmesi*: Gemini 1.5 Flash’ın ürettiği sonuçlar bir araya getirilip Gemini 1.5 Pro modelinde bir bütün şeklinde inceleniyor. Tespit edilen yanlışlıklar ve üretilen sorular algılanan duygu ve konuşma biçimi ile birleşip tek bir sonuca dönüştürülüyor. Ardından Google Text to Speech kullanılarak karakterimiz konuşmaya başlıyor.


Toplantılar, açık kaynak bir araç kullanılarak kendi sunucumuzda gerçekleştiriliyor; bu sayede harici bir toplantı servisine ihtiyaç duyulmadan tüm kontroller bizde ve etik kurallar çerçevesinde gerçekleşiyor



# EduMeet

EduMeet is a meeting platform equipped with artificial intelligence to make your presentations a pain in the ass. Unlike platforms with only humans, EduMeet takes your presentations to a different dimension with powerful technologies behind Gemini and other Google Cloud Projects products. All you need to do to use it is to choose [edumeet.tech](http://edumeet.tech) as your meeting platform.

## Features

- *Artificial Intelligence Powered Character*: Our Gemini-powered character accompanies you during the meeting, attends your meeting, monitors your screen sharing, detects and understands you if your camera and microphone are on.
- *Correcting Incorrect Information*: Corrects incorrect information you relay by speaking out loud to you at that moment.
- Interactive Questions*: It asks you questions aloud on the topic you are talking about.
- Facial Expression and Voice Analysis*: In addition to the topic you are talking about, it communicates with you by detecting the way you speak and your facial expression.

## How does it work?

EduMeet pays attention to the accuracy of the information conveyed within the framework of its principles, the harmony between the materials used by the presenter and what they tell, and asking questions on the subject to enrich the information conveyed. The answers are prepared live during the meeting according to the presenter's speech style and facial expression, and are transmitted aloud through our artificial intelligence character.


#### Process Stages

1. *Facial Expression Detection*: Google Vision's Face Detection feature detects the individual in the given image and provides the data that needs to be interpreted from the facial expression. The incoming data is quickly interpreted by Gemini 1.5 Flash and converted into a single emotional expression.

2. *Interpretation of Audio Data*: Thanks to Gemini's ability to detect the given audio file, the audio data is sent to be analyzed. Here, Gemini interprets the way the speaker speaks and analyzes what is being said, scanning for topics and misinformation. Then, a question is generated by specifying the topic and misinformation.

3. *Shared Image Detection*: The screen data obtained is parsed and detected using Google Video Intelligence and Google Vision with Text Detection, Label Detection and Speech Transcription features. The data obtained is analyzed using Gemini according to its accuracy and compatibility with each other, and the reasons for the detected misinformation and incompatibilities are stated, and questions are also generated.

4. *Combining the Results*: The results produced by Gemini 1.5 Flash are brought together and analyzed as a whole in the Gemini 1.5 Pro model. The inaccuracies detected and the questions generated are combined with the perceived emotion and speech style and converted into a single result. Then, using Google Text to Speech, our character starts to speak.

Meetings are held on our own server using an open source tool, so we have all the controls and ethics in place without the need for an external meeting service




