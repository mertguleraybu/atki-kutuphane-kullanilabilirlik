# Agent - Otonom Web Gezinme Modülü

Bu klasör, tezin deneysel aşamasında kullanılan ve kütüphane web sitesi üzerinde tanımlanan görev senaryolarını adım adım yürüten otonom yapay zekâ ajanının kaynak kodlarını barındırmaktadır. Ajan, doğal dilde verilen talimatları web ortamında işlevsel eylemlere dönüştürmek üzere Akıl Yürütme ve Eyleme Geçme (Reasoning and Acting - ReAct) döngüsünü kullanır.

---

## Bağımlılıklar ve Ön Gereksinimler

Sistem, Python kütüphanelerinin yanı sıra sistem düzeyinde çalışan harici bir büyük dil modeli (LLM) servis sağlayıcısına ihtiyaç duyar. Bu nedenle kurulum işlemleri iki aşamalıdır.

### 1. Sistem Düzeyinde Ön Gereksinim: Ollama
Bu projedeki yerel büyük dil modelleri (LLaMA 3 ve Mistral 7B) harici API servislerine bağımlılığı ortadan kaldırmak ve deney ortamını tamamen kontrol altında tutabilmek amacıyla yerel donanımda **Ollama** arayüzü ile çalıştırılmıştır. 

Ollama bir Python kütüphanesi olmadığı için `requirements.txt` dosyasında yer almaz. Kodları çalıştırmadan önce sisteminizde Ollama'nın kurulu ve arka planda aktif olması gerekmektedir:

1. https://ollama.com adresinden işletim sisteminize uygun sürümü indirip kurun.
2. Komut satırından projede kullanılan modelleri sisteminize çekin:
   ```bash
   ollama run llama3
   ollama run mistral