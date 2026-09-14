# SkillBridge 🚀

**Know Your Career. Build Your Skills. Land Your Dream Job.**

SkillBridge is a modern, responsive, zero-dependency career guidance and skill-gap analysis platform built specifically for students and early-career professionals. It helps users discover industry-required skills, assess their current proficiency, and generates a personalized, highly actionable learning roadmap to bridge the gap.

## 🎯 The Problem
Many students choose careers without truly understanding the specific skills required for their desired jobs. They are often unaware of the gap between their current capabilities and actual industry expectations, leading to inefficient learning and missed opportunities.

## 💡 The Solution
SkillBridge solves this by providing a hyper-focused, transparent assessment tool. By comparing a user's self-assessed skills against real-world job requirements, SkillBridge eliminates the guesswork and tells the user exactly what to learn, in what order, and where to learn it.

---

## ✨ Features

- **Career Explorer**: Explore high-demand roles including Software Developer, Data Analyst, UX/UI Designer, Digital Marketer, AI Engineer, Cybersecurity Analyst, and Product Manager.
- **Granular Skill Assessment**: Rate your proficiency on a 1-5 scale across highly specific, industry-relevant skills (e.g., CI/CD Basics, MLOps, Figma, SEO).
- **Dual-Metric Analysis Engine**:
  - **Match Score**: Calculates how closely you meet the baseline job requirements.
  - **Productivity Score**: Measures your overall efficiency. If your skills exceed the baseline requirements, your productivity score scales past 100%.
- **Actionable Roadmaps**: Automatically generates a prioritized, step-by-step learning path for your missing and developing skills, complete with dynamic **Time Estimates** and tailored **Real-world Resource Recommendations** (e.g., *Frontend Masters*, *SQLZoo*, *HubSpot Academy*).
- **Radiant Dark Mode**: A stunning, custom-built dark theme featuring deep radiant gradients and glowing accents for late-night studying.
- **Privacy First**: 100% client-side application. No logins, no databases, all assessment data is securely stored in your local browser.

---

## 🛠️ Technology Stack

SkillBridge is built as a highly optimized, lightweight MVP without the bloat of modern frameworks.

- **Frontend**: HTML5, Semantic UI
- **Styling**: Vanilla CSS3 (Custom Properties/Variables, Flexbox, CSS Grid)
- **Logic**: Vanilla JavaScript (ES6+)
- **State Management**: Browser `localStorage` API
- **Dependencies**: None. Zero external frameworks (No React, Vue, or Angular).

---

## 🚀 Getting Started

Because SkillBridge is a vanilla HTML/JS application, running it is incredibly simple.

### Prerequisites
- A modern web browser (Chrome, Firefox, Edge, Safari)
- (Optional) A local HTTP server for the best experience.

### Installation & Execution

1. **Clone the repository** (or download the source code):
   ```bash
   git clone https://github.com/yourusername/skillbridge.git
   cd skillbridge
   ```

2. **Run a local server** (Recommended):
   If you have Python installed, you can easily spin up a local server:
   ```bash
   python -m http.server 8000
   ```
   Then navigate to `http://localhost:8000` in your browser.

3. **Alternative**: 
   Simply double-click `index.html` to open it directly in your web browser.

---

## 📂 Project Structure

```text
skillbridge/
├── css/
│   └── style.css       # Master stylesheet (Light/Dark themes, components, layouts)
├── js/
│   ├── app.js          # Core analysis engine, state management, and theme logic
│   └── data.js         # Career database, skill requirements, and importance weights
├── index.html          # Landing page and Dashboard mockups
├── careers.html        # Career exploration grid
├── assess.html         # Interactive 1-5 skill assessment tool
├── dashboard.html      # Results dashboard and dynamic roadmap generation
└── README.md           # Project documentation
```

---

## 🔮 Future Roadmap (Post-Hackathon)
- **User Authentication**: Allow users to create accounts to sync their roadmaps across devices.
- **API Integrations**: Connect with Udemy, Coursera, or YouTube APIs to pull live course data and pricing.
- **Progress Tracking**: Allow users to check off roadmap items and see their Match Score increase over time.

---

*Built with ❤️ for the "Build a Digital Solution for a Real Community Problem" Hackathon.*
