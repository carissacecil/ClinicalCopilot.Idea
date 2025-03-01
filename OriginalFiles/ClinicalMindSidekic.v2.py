
class ClinicalMindSidekick:
    def __init__(self):
        self.resources = {
            "continuing_education": [
                {"title": "Cultural Competency in Mental Health", "details": "An online course offering 4 CEU credits."},
                {"title": "Advanced Grief Counseling Strategies", "details": "In-person workshop offering 6 CEU credits."}
            ],
            "pertinent_research": [
                {"title": "Cultural Dimensions of Grieving in Hispanic Families",
                 "summary": "Explores the grieving process specific to Hispanic cultural contexts.",
                 "details": "Insights include traditional practices and the role of family. Offers guidance on culturally sensitive interventions."},
            ],
            "cross_collaboration": [
                {"title": "Hispanic Family Grief Support Group",
                 "details": "Monthly meetings with professionals focused on Hispanic grief support."}
            ]
        }

    def list_capabilities(self):
        print("\nClinicalMindSidekick Capabilities: ")
        print("1. Provide Continuing Education Opportunities")
        print("2. Share Pertinent Research")
        print("3. Facilitate Cross-Collaboration and Consultation")
        print("4. Act as a Consultant on Clinically Proven Interventions\n")

    def provide_resources(self, user_query):
        print(f"\nFetching resources for: {user_query}\n")
        for key, items in self.resources.items():
            for item in items:
                if user_query.lower() in item['title'].lower():
                    print(f"**{item['title']}**")
                    if key == "pertinent_research":
                        print(f"Summary: {item['summary']}")
                    print(f"Details: {item['details']}\n")

    def respond_to_consultation_request(self, consultation_query):
        if "grieving a child for a client that are tailored to hispanic families and culture" in consultation_query.lower():
            print("\nConsultation Resource Recommendation: ")
            print("**Cultural Dimensions of Grieving in Hispanic Families**\nDetails: Offers guidance on culturally sensitive interventions tailored for Hispanic families. Includes traditional practices and the role of extended family.\n")
        else:
            print("Sorry, I don't have consultation resources for that specific request at the moment.")

def main():
    print("Welcome to ClinicalMindSidekick!")
    
    cms = ClinicalMindSidekick()
    cms.list_capabilities()

    while True:
        user_query = input("You: ").strip()
        
        if user_query.lower() == "exit":
            print("Thank you for using ClinicalMindSidekick. Goodbye!")
            break
        elif "resources on" in user_query.lower():
            cms.provide_resources(user_query)
        elif "i need" in user_query.lower():
            cms.respond_to_consultation_request(user_query)
        else:
            print("How may I assist you today? You can ask for resources, consultation, or information on our capabilities.")

if __name__ == "__main__":
    main()
