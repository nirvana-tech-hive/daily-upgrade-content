# 🎨 CSS Theme Template for Daily Upgrade Content Engine

---

## **📌 Overview**
This template provides a **consistent, responsive, and light-themed CSS design** for all HTML blog posts in the **Daily Upgrade Content Engine**. It ensures **visual consistency**, **mobile optimization**, and **scalability** while preserving the narrative, flow, originality, structure, and integrity of your content.

---

## **📁 File Location**
`content/templates/CSS_THEME_TEMPLATE.md`

---

## **📌 How to Use This Template**

### **1️⃣ For New Blog Posts**
When creating the **HTML version (`post.html`)** of a blog post:
- Copy the **entire HTML code block** from this template.
- Replace the **placeholder content** (titles, text, images, buttons) with your **actual blog post content**.
- Ensure all **CSS variables** (colors, fonts) are preserved as-is.
- Use the **scoped styles** (prefixed with `#career-article-container`) to prevent conflicts with global site styles.

---

### **2️⃣ For Existing Blog Posts**
When updating the **HTML version (`post.html`)** of an existing blog post:
- Open the `post.html` file.
- Locate the `<style>` section.
- Replace the **entire `<style>` block** with the CSS code from this template.
- Ensure all **CSS variables** (colors, fonts) are preserved as-is.
- Update the **content sections** (titles, text, images, buttons) with your **actual blog post content**.

---

### **3️⃣ For Consistency Across All Posts**
- Use this template **for every new HTML blog post** you create.
- Store this template in the `content/templates/` folder for easy access.
- Reference this template in your **CONTENT_CREATION_SEQUENCE.md** to ensure consistency.

---

## **📌 Template Structure**

The template is structured as a **complete HTML document** with:

1. **Scoped CSS Styles** (prefixed with `#career-article-container`)
   - Light theme colors (Navy Blue, Gold, White, Light Gray)
   - Clean sans-serif typography (Segoe UI, system fonts)
   - Card-based sections with rounded corners (12px-20px) and subtle shadows
   - Gold accents for borders, icons, or important text

2. **Mobile Optimization**
   - Single column layout for mobile devices
   - Proper text alignment and no horizontal scroll
   - Responsive breakpoints for tablets and larger screens

3. **Interactivity**
   - Vanilla JavaScript for simple interactions (e.g., scroll reveals)
   - Respects `prefers-reduced-motion` for accessibility
   - No external dependencies

4. **Content Flow Assistance**
   - **PAS + Playbook Framework** structure:
     - Hook (Problem)
     - Agitate (Deepens the problem)
     - Reframe (Shifts the mindset)
     - Solution Overview (Introduces core philosophy)
     - Practical Playbook (Details 3-5 specific skills)
     - Future Outlook (Discusses human-AI collaboration)
     - Weekly Action Plan (Provides a specific 7-day plan)
     - Reflective Conclusion (Leaves the reader motivated)

---

## **📌 CSS Variables (Do Not Change)**

```css
#career-article-container {
  --navy-deep: #0d1b2a;
  --navy-mid: #1b263b;
  --navy-light: #415a77;
  --gold-primary: #c9a227;
  --gold-light: #e8d48b;
  --cream: #f8f9fa;
  --white: #ffffff;
  --text-primary: #1a1a2e;
  --text-secondary: #4a5568;
  --text-muted: #6b7280;
  --border-light: #e5e7eb;
  --shadow-soft: rgba(13, 27, 42, 0.08);
  --shadow-medium: rgba(13, 27, 42, 0.15);
  --shadow-strong: rgba(13, 27, 42, 0.25);
}
```

---

## **📌 How to Integrate This Template**

### **1️⃣ For the HTML Version of a Blog Post**
When creating the `post.html` file for a blog post:

1. Copy the **entire HTML code block** from this template.
2. Open the `post.html` file for your blog post.
3. Replace the **entire content** of the `post.html` file with the copied HTML code block.
4. Update the following sections with your **actual blog post content**:
   - `<title>`
   - `<h1>` (article title)
   - `<p class="intro-hook">` (introductory hook)
   - `<section>` content (Hook, Agitate, Reframe, Solution Overview, Practical Playbook, Future Outlook, Weekly Action Plan, Reflective Conclusion)
   - `<figure class="hero-figure">` (hero image)
   - `<figure class="support-figure">` (support images)
   - `<button class="cta-button">` (CTA button text)

5. Ensure all **CSS variables** (colors, fonts) are preserved as-is.

6. Use the **scoped styles** (prefixed with `#career-article-container`) to prevent conflicts with global site styles.

---

### **2️⃣ For Consistency Across All Posts**
- Store this template in the `content/templates/` folder.
- Reference this template in your **CONTENT_CREATION_SEQUENCE.md** to ensure consistency.
- Use this template **for every new HTML blog post** you create.

---

## **📌 Example Integration**

### **For Brain Upgrade #1**
1. Copy the **entire HTML code block** from this template.
2. Open the `post.html` file for Brain Upgrade #1.
3. Replace the **entire content** of the `post.html` file with the copied HTML code block.
4. Update the following sections with your **actual blog post content**:
   - `<title>`: "Brain Upgrade #1: The Dangers of AI Dependency"
   - `<h1>`: "Brain Upgrade #1: The Dangers of AI Dependency"
   - `<p class="intro-hook">`: "AI is making us lazy..."
   - `<section>` content: Use the rich, detailed content from your `post.md` file.
   - `<figure class="hero-figure">`: Add your hero image URL.
   - `<figure class="support-figure">`: Add your support image URLs.
   - `<button class="cta-button">`: "Start Your Brain Upgrade Today"

5. Ensure all **CSS variables** (colors, fonts) are preserved as-is.

6. Use the **scoped styles** (prefixed with `#career-article-container`) to prevent conflicts with global site styles.

---

## **📌 Template Storage**

This template is now stored in your repository at:
`content/templates/CSS_THEME_TEMPLATE.md`

---

## **📌 Next Steps**

1. **Use this template** for every new HTML blog post you create.
2. **Store this template** in the `content/templates/` folder for easy access.
3. **Reference this template** in your **CONTENT_CREATION_SEQUENCE.md** to ensure consistency.
4. **Integrate this template** into your **HTML version creation workflow**.

---

**Let me know if you'd like to add more details or customize the template further!** 🚀