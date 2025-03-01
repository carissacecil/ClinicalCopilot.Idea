from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "There’s such a compelling argument for this kind of tool and people will do this regardless with GPT once it becomes more common as a resource — so having it be designed as a HIPAA safe and LLM that’s trained and streamlining the kinds of unique support a therapist needs that all seems like the angle ?\nAlso I think the juicy part for me is the idea that the therapist gets their own sanctioned relational alliance —  while they themselves are being utilized across all their client care relationships they have a support and ally with the clinical experience to diminish the ambient stress and loneliness of the profession. \n\nI’m imagining a dashboard where I can identify the kinds of client I see (demographics), the style of therapy I practice, interventions I’m trained in — and then choosing the top needs I want support around in my practice of the following for example: 1) crisis management and resources 2) continuing education 3) processing my own countertransference (emotional experiences and activation in sessions) 4) improving my skills (language?) related to cultural competency/sexuality/high-risk behaviors 5) treatment planning  6) progress notes and insurance claim filing …. \n\nBAHAHAHAHAH.   ---- and If an LLM trained MH therapy co-pilot was consistently bringing that kind of question into the space for the therapist to consider like every once in a while my TherapySiri was like —— hey Jocelyn, I wonder how the client’s intergenerational trauma and cultural experience could impact how effective XYZ intervention would be, or have you considered this continuing education course given the client is Latinx?, or their suicidality risk is heightened due to culture/race…. That’s all helpful\nThe case example for me on this is I was serving a high risk Client having a crisis and I could NOT get support or supervision fast enough and it was SO STRESSFUL and led to my major burnout. If I had had chatGPT back then I would have been talking to it constantly and seeking advice and resources. If I had a trustworthy ally all times of day that could hold the client care WITH me - incredible.\n\nAwesome if this helps — “I am a therapist. I just had a session and I’m fully licensed, I don’t have a clinical supervisor overseeing me but I am concerned about a client’s safety based on what they reported tonight and I didn’t do as full of an overall assessment of risk over the past couple months both intake and in daily meetings — HEY THERAPY SIRI help me do a risk assessment based on what you know of the clients demographics (e.g. I use Jeffrey Sung’s great risk assessment) and develop nex steps” ---- “I am a therapist and I haven’t done my continuing educaiton in a while —— HEY THERAPY SIRI set up a reminder and do some research on local CEUs on eating disorders” ——— “I am a therapist and I think I should be doing some deeper OCD treatment with a client but I’m not trained in it -- hey therapy Siri,  help me understand the basics and think on integrating it based on XYZ factors about this client” —— “Hey Therapy Siri I just had a session with “dorothy” again and Ifeel really weird about it….. I just don’t feel good after it...can you help me process? (SYNETHIC AI THERAPIST FOR A THERAPIST - GO!)” see there’s so many applications for a sidekick …. Gah!\n\n\nBe the assistant -- i will talk you "
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "It sounds like you are envisioning a highly specialized, AI-driven co-pilot to support therapists in their practice, addressing a variety of needs while maintaining HIPAA compliance. The concept combines the capabilities of large language models (LLMs) with specific adaptations and features designed to enhance clinical practice. Here's a breakdown of some key ideas and potential features:\n\n1. **Supportive Alliance for Therapists**: This AI tool would act as a supportive partner for therapists, offering guidance, resources, and a sense of shared burden to mitigate the stress and isolation that can accompany therapeutic work.\n\n2. **Customizable Dashboard**: A personalized interface where therapists can input their demographics, therapeutic style, interventions, and areas where they seek support. This customization would ensure that the AI provides relevant and targeted assistance.\n\n3. **Priority Areas for Support**: Features could include:\n   - **Crisis Management**: Immediate access to resources and support for handling high-risk or urgent situations.\n   - **Continuing Education**: Recommendations for CEUs and courses tailored to the therapist’s interests and gaps in expertise.\n   - **Countertransference Processing**: A safe space for therapists to reflect on their emotional responses and experiences with clients.\n   - **Cultural Competency**: Resources and guidance on enhancing skills related to cultural sensitivity, understanding, and specific client demographics.\n   - **Treatment Planning**: Assistance in formulating and fine-tuning treatment plans based on best practices and client data.\n   - **Administrative Support**: Streamlined tools for progress notes, insurance claims, and documentation.\n\n4. **Interactive and Proactive Engagement**: The AI tool would not only respond to prompts but also actively engage the therapist by asking insightful questions and suggesting resources. For example, prompting considerations of cultural factors in interventions or recommending specific training courses.\n\n5. **On-Demand Risk Assessments**: The ability to perform comprehensive risk assessments using established frameworks and provide step-by-step guidance on next steps for client safety.\n\n6. **Therapist Self-Care**: Tools for therapists to process their own feelings, stress, and experiences, perhaps through reflective exercises or prompts.\n\n7. **Confidence in AI as a Resource**: By focusing on creating a trustworthy, reliable, and informed AI partner, therapists can feel more at ease turning to it for support, ultimately preventing burnout.\n\nYour concept is both innovative and practical, addressing real gaps in therapist support by utilizing the advancements in AI. This kind of tool could revolutionize the way therapists operate, making their work more sustainable and effective."
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "How can I help you further with this idea? Are there specific features or functionalities you'd like to explore, or any considerations you'd like advice on?"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "can i talk to you as if you are the co-pilot?\n"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "Of course! I'm here to assist you just like the AI therapy co-pilot you've envisioned. How can I support you today?"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "I had a hard session - I'm worried about \"karen\"\n"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "I'm here to help you process and find the best course of action. Can you tell me a bit more about what happened in the session that raised your concerns about Karen?"
        }
      ]
    }
  ],
  response_format={
    "type": "text"
  },
  temperature=1,
  max_completion_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)