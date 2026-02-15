# Deploying Smart Portfolio Rebalancer 🚀

Congratulations on building a cutting-edge AI financial tool! Here is how to deploy it for the hackathon judges.

## Option 1: Vercel (Recommended - Easiest)
Vercel is the creators of Next.js and offers the best Zero-Config deployment for Vite apps.

1.  **Create a GitHub Repo**:
    -   Go to [github.com/new](https://github.com/new).
    -   Name it `smart-portfolio-ai`.
    -   Do **NOT** initialize with README/gitignore (we already have them).
    -   Click **Create repository**.

2.  **Push Code**:
    Open your terminal in the `smart-portfolio` folder and run:
    ```bash
    git add .
    git commit -m "Hackathon Final Build"
    git branch -M main
    git remote add origin https://github.com/YOUR_USERNAME/smart-portfolio-ai.git
    git push -u origin main
    ```

3.  **Deploy on Vercel**:
    -   Go to [vercel.com/new](https://vercel.com/new).
    -   Import your `smart-portfolio-ai` repo.
    -   **Framework Preset**: Vite (Automatic).
    -   Click **Deploy**.
    -   🎉 **Result**: You get a live URL (e.g., `smart-portfolio-ai.vercel.app`) in seconds.

## Option 2: GitHub Pages (Free)
If you prefer to stay purely on GitHub.

1.  **Update `vite.config.ts`**:
    Add `base: '/smart-portfolio-ai/'` (replace with your repo name) to the config object.

2.  **Push Code** (same as above).

3.  **Enable Pages**:
    -   Go to Repo Settings > Pages.
    -   Source: `GitHub Actions`.
    -   Use the "Static HTML" workflow.

## Option 3: Docker (Containerized)
Ideal for deploying to AWS ECS, DigitalOcean, Azure, or running locally in an isolated environment.

1.  **Build and Run**:
    Run the following command in the root of your project:
    ```bash
    docker-compose up --build
    ```

2.  **Access the App**:
    Open [http://localhost:8080](http://localhost:8080) to see your app running in a container.

3.  **Deployment**:
    - Push your code (including `Dockerfile` and `docker-compose.yml`) to your repo.
    - Connect your repo to your cloud provider's container service.
    - Alternatively, pull the code on a VPS and run `docker-compose up -d`.

## Option 4: Manual / Local Presentation
If internet fails, you can run the localized production build:

1.  Run `npm run build`.
2.  Run `npm run preview`.
3.  Open `http://localhost:4173`.
   
   This mimics a real production server locally!

---
**Hackathon Tip**: Use `Option 1` (Vercel). It provides the fastest CDN and best performance for the "Cutting Edge" feel.
