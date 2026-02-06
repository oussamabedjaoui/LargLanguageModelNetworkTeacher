# 🎓 LLM Network Teacher - Professeur IA de Réseaux Informatiques

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-green.svg)](https://ollama.ai)

## 📖 Description du Projet

**LLM Network Teacher** est un assistant pédagogique intelligent spécialisé dans l'enseignement des **réseaux informatiques**. Ce projet utilise un **Large Language Model (LLM)** personnalisé, fine-tuné pour répondre exclusivement aux questions liées aux réseaux, tout en adoptant un ton encourageant et pédagogique.

### 🎯 Objectifs

- **Éducation accessible** : Fournir des explications claires et simples sur les concepts réseaux
- **Focus spécialisé** : Le modèle refuse poliment les questions hors sujet pour rester concentré sur sa mission éducative
- **Apprentissage interactif** : Interface conversationnelle intuitive pour un apprentissage naturel

---

## ✨ Fonctionnalités

| Fonctionnalité | Description |
|----------------|-------------|
| 💬 **Chat interactif** | Interface de conversation en temps réel avec streaming des réponses |
| 🧠 **LLM personnalisé** | Modèle GGUF optimisé pour l'enseignement des réseaux |
| 🎯 **Réponses ciblées** | Refuse automatiquement les questions hors sujet |
| 📚 **Ton pédagogique** | Explications encourageantes avec exemples concrets |
| 🔒 **100% Local** | Aucune donnée envoyée vers le cloud, tout fonctionne en local |

---

## 🏗️ Architecture Technique

```
┌─────────────────────────────────────────────────────────────┐
│                    Interface Utilisateur                     │
│                      (Streamlit Web App)                     │
├─────────────────────────────────────────────────────────────┤
│                    Application Python                        │
│                        (app.py)                              │
│  • Gestion de l'historique de conversation                  │
│  • Injection du prompt système                              │
│  • Nettoyage des réponses en temps réel                     │
├─────────────────────────────────────────────────────────────┤
│                      Ollama Runtime                          │
│                   (Serveur LLM Local)                        │
├─────────────────────────────────────────────────────────────┤
│                    Modèle Personnalisé                       │
│                      (prof.gguf)                             │
│           Fine-tuné pour l'enseignement réseaux             │
└─────────────────────────────────────────────────────────────┘
```

### 📁 Structure des Fichiers

```
LargLanguageModelNetworkTeacher/
├── Mon_Bot_Prof/
│   ├── app.py          # Application Streamlit principale
│   ├── Modelfile       # Configuration du modèle Ollama
│   └── prof.gguf       # Modèle LLM (à télécharger séparément)
├── .gitignore          # Fichiers exclus du repo
└── README.md           # Documentation
```

---

## 🚀 Installation

### Prérequis

- **Python 3.8+**
- **Ollama** installé sur votre machine ([Télécharger Ollama](https://ollama.ai))
- **4+ GB de RAM** disponible pour le modèle

### Étape 1 : Cloner le Repository

```bash
git clone https://github.com/oussamabedjaoui/LargLanguageModelNetworkTeacher.git
cd LargLanguageModelNetworkTeacher/Mon_Bot_Prof
```

### Étape 2 : Télécharger le Modèle

⚠️ **Le fichier `prof.gguf` (4.17 GB) n'est pas inclus dans le repository.**

Téléchargez-le depuis :
> 🔗 **[Hugging Face - prof-network-LLM](https://huggingface.co/Oussamabedjaoui/prof-network-LLM/resolve/main/prof.gguf)**

Placez le fichier `prof.gguf` dans le dossier `Mon_Bot_Prof/`.

### Étape 3 : Installer les Dépendances Python

```bash
pip install streamlit ollama
```

### Étape 4 : Créer le Modèle dans Ollama

```bash
ollama create mon-prof -f Modelfile
```

### Étape 5 : Lancer l'Application

```bash
streamlit run app.py
```

L'application sera accessible sur **http://localhost:8501**

---

## 💡 Utilisation

### Exemples de Questions Supportées

✅ **Questions Réseaux (Réponses détaillées)**
- "C'est quoi un routeur ?"
- "Explique-moi le modèle OSI"
- "Quelle est la différence entre TCP et UDP ?"
- "Comment fonctionne le protocole DHCP ?"
- "C'est quoi une adresse IP ?"

❌ **Questions Hors Sujet (Refusées poliment)**
- "Qui est Napoléon ?" → *"Je ne sais pas, je suis un prof de réseaux."*
- "Fais-moi une blague" → *"Je ne sais pas, je suis un prof de réseaux."*
- "Quelle est la recette du gâteau au chocolat ?" → *"Je ne sais pas, je suis un prof de réseaux."*

---

## ⚙️ Configuration du Modèle

Le fichier `Modelfile` définit le comportement du LLM :

```
FROM ./prof.gguf

PARAMETER temperature 0.6    # Créativité modérée
PARAMETER num_ctx 4096       # Contexte de 4096 tokens

SYSTEM """
Tu es un Professeur de Réseaux Informatiques passionné...
"""
```

### Paramètres Ajustables

| Paramètre | Valeur | Description |
|-----------|--------|-------------|
| `temperature` | 0.6 | Contrôle la créativité (0 = déterministe, 1 = créatif) |
| `num_ctx` | 4096 | Taille du contexte en tokens |

---

## 🛠️ Technologies Utilisées

- **[Streamlit](https://streamlit.io)** - Framework Python pour les interfaces web
- **[Ollama](https://ollama.ai)** - Runtime pour exécuter des LLMs en local
- **[GGUF](https://github.com/ggerganov/ggml)** - Format de modèle optimisé pour l'inférence CPU/GPU

---

## 📊 Caractéristiques du Modèle

| Propriété | Valeur |
|-----------|--------|
| Format | GGUF |
| Taille | ~4.17 GB |
| Spécialisation | Réseaux Informatiques |
| Langue | Français |
| Exécution | 100% Local |

---

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. **Fork** le projet
2. Créer une **branche** (`git checkout -b feature/amelioration`)
3. **Commit** vos changements (`git commit -m 'Ajout d'une fonctionnalité'`)
4. **Push** vers la branche (`git push origin feature/amelioration`)
5. Ouvrir une **Pull Request**

---

## 📜 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 👨‍💻 Auteur

**Oussama Bedjaoui**

- GitHub: [@oussamabedjaoui](https://github.com/oussamabedjaoui)

---

## 🙏 Remerciements

- L'équipe **Ollama** pour leur excellent runtime LLM
- **Streamlit** pour leur framework simple et puissant
- La communauté open-source pour les modèles GGUF

---

<p align="center">
  <b>🎓 Apprendre les réseaux n'a jamais été aussi simple !</b>
</p>
