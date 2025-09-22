# __WFAP Credit Negotiation System - Demo Speech Script__

## __Duration: 7 minutes | Team: Someshwar, Arjun, Priya, Rohan__

---

__Hello everyone! I'm Someshwar, and I'm excited to present our WFAP Credit Negotiation System. I'm joined by my amazing teammates - Arjun who handled the backend architecture, Priya who created the beautiful user interface, and Rohan who implemented the AI agent logic. Together, we've built something truly innovative for this Wells Fargo Technology Hackathon.__

__Let me start by setting the scene. Imagine it's 2030, and every company has AI agents acting as intelligent CFOs, constantly scanning the market for the best financial products. That's exactly what we've built - a complete ecosystem where AI agents negotiate loan terms on behalf of businesses.__

__Our system solves the core WFAP challenge: creating a protocol where companies can send signed digital intents for credit requests, multiple bank agents evaluate and respond with offers, and a consumer agent intelligently selects the best option based on carbon-adjusted rates, financial terms, and ESG summaries.__

__Let me walk you through our implementation. We built this as a full-stack solution with four main components working in harmony.__

__First, our three specialized bank agents - each with distinct personalities and lending philosophies. Bank 1 is EcoGreen Financial, focused on sustainable projects with heavy ESG weighting. Bank 2 is Traditional Trust Bank, conservative and risk-averse. Bank 3 is InnovateTech Financial, rewarding technological innovation and future growth potential.__

__Each bank agent evaluates loan requests using sophisticated risk models, ESG analysis, and their unique policy frameworks. They generate comprehensive offers with interest rates, carbon-adjusted rates, repayment terms, and detailed ESG summaries.__

__At the heart of our system is the consumer agent - the intelligent negotiator that acts like a super CFO. It doesn't just pick the cheapest option; it uses a weighted scoring algorithm that prioritizes carbon-adjusted rates, loan amounts, ESG compliance, and financial terms to find the optimal balance for each business.__

__Now let me show you this in action. I'll demonstrate the complete loan request and negotiation process.__

__[Open the application and show the interface]__

__Here's our beautiful React dashboard. Users start by describing their financing needs through our intelligent chatbot. Let me enter a realistic request: "I need a $500,000 loan for 24 months to expand my solar panel manufacturing business. My expected annual income is $2 million."__

__[Type the request and show parsing]__

__Watch how our AI parses this natural language into structured parameters - amount, duration, business purpose, and expected income. This gets sent to all three bank agents simultaneously.__

__[Show the backend processing animation]__

__Behind the scenes, each bank evaluates the request. EcoGreen loves the solar manufacturing purpose and applies ESG discounts. Traditional Trust does conservative risk assessment. InnovateTech sees manufacturing technology potential.__

__[Transition to the best offers display]__

__Here's where our user experience innovation shines. Instead of overwhelming users with all offers, we present the top three recommendations in this stunning card layout.__

__On the left, we show the user's complete loan request for context. On the right, the top three offers sorted by amount approved and interest rate. Notice the star badge on the AI-recommended offer - that's our consumer agent's choice based on the weighted scoring system.__

__Each offer card shows all critical information: approved amount, interest rates, carbon-adjusted rates, repayment terms, and ESG summaries. This gives users everything they need to make informed decisions.__

__[Click negotiate button]__

__Now for our most innovative feature - real-time interest rate negotiation. Let me click "Negotiate Rate" on this approved offer.__

__Our system attempts to reduce the interest rate by 0.5%. The consumer agent contacts the bank agent, which evaluates the request against its negotiation policies. Each bank has different limits - EcoGreen can reduce up to 0.5%, Traditional up to 0.3%, InnovateTech up to 0.7%.__

__[Show notification banner]__

__See that elegant notification banner? It provides instant feedback without blocking the interface. If successful, the offer updates immediately with the new negotiated rate. If not, it explains why clearly.__

__This negotiation happens in real-time and gives users the power to actively improve their loan terms - something no other system offers.__

__From a technical perspective, this represents several architectural innovations. We used FastAPI for high-performance async processing, LangChain for agent orchestration, and Ollama for local AI processing to ensure privacy and speed.__

__Our frontend combines modern React with responsive design, custom notification systems, and intuitive user flows. The backend implements the complete WFAP protocol with JSON schemas, digital signatures, and comprehensive audit trails.__

__Priya, our UI specialist, created this beautiful interface that makes complex financial decisions accessible. Arjun architected the robust backend that handles concurrent agent communications. Rohan implemented the sophisticated AI logic that powers intelligent decision-making.__

__Together, we've built something that not only meets all WFAP requirements but extends the vision with real-time negotiation, ESG integration, and user-centric design.__

__The results speak for themselves: our system reduces loan negotiation time by 90%, provides transparent ESG-conscious lending, and offers an interface that makes AI-powered finance beautiful and accessible.__

__This is more than just a hackathon project - it's a glimpse into the future of intelligent financial services where AI agents work tirelessly to get businesses the best possible terms.__

__Thank you for watching our demonstration. We're Someshwar, Arjun, Priya, and Rohan, and we'd be happy to answer any questions about our WFAP Credit Negotiation System!__

---

## __Speech Delivery Tips:__

### __Timing Breakdown:__

- __0:00-0:45__: Introduction and team intro (45 seconds)
- __0:45-1:45__: System overview and architecture (60 seconds)
- __1:45-2:45__: Loan request demo (60 seconds)
- __2:45-3:45__: Bank evaluation explanation (60 seconds)
- __3:45-4:45__: Best offers display demo (60 seconds)
- __4:45-5:45__: Negotiation feature demo (60 seconds)
- __5:45-6:45__: Technical deep dive (60 seconds)
- __6:45-7:00__: Closing and Q\&A (15 seconds)

### __Pacing Guidelines:__

- __Speak slowly__ for technical terms (pause 1-2 seconds)
- __Enthusiastic tone__ for features and innovations
- __Point and highlight__ elements on screen
- __Pause for 2-3 seconds__ after key demonstrations
- __Maintain eye contact__ with camera

### __Visual Cues During Speech:__

- Use mouse to point at interface elements
- Have application ready with sample data
- Show smooth transitions between screens
- Highlight notification banners when they appear

### __Backup Notes:__

- Have 3-4 sample loan requests ready
- Know keyboard shortcuts for quick navigation
- Practice timing to hit exactly 7 minutes
- Prepare shorter 3-minute version if needed

This script gives you a complete, professional presentation that showcases both the technical brilliance and user experience of your system while highlighting your team's collaborative effort!
