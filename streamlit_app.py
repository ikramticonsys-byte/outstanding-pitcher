import google.generativeai as genai
import streamlit as st

st.set_page_config(page_title="Global AI Job Pitcher", page_icon="🚀")
st.title("🚀 Global AI Job Pitch & Reply Generator")
st.write("Craft responses so impressive that employers cannot ignore you!")

st.info("💡 How to get a FREE Gemini API Key? Go to https://google.com and click 'Get API Key'. It takes only 1 minute!")

api_key = st.text_input("Enter your Free Gemini API Key:", type="password")
job_desc = st.text_area("Paste the Job Description or Owner's Post here:", height=150)
user_skills = st.text_area("Enter your Skills, Experience, or Bio:", height=150)

if st.button("Generate Outstanding Reply ✨"):
    if api_key and job_desc and user_skills:
        with st.spinner("Analyzing and drafting your ultimate pitch..."):
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-pro')
                
                prompt = f"""
                You are the world's best Executive Headhunter. 
                Job Description/Owner's Post: {job_desc}
                Candidate Skills/Bio: {user_skills}
                
                Task: Write an exceptional, highly impressive, and outcome-driven application reply/pitch. 
                Make it brief but punchy. Catch the owner's attention in the first 2 sentences. 
                Propose a clear solution using the candidate's expertise. 
                Make the owner feel that NOT hiring this person would be a massive loss.
                """
                
                response = model.generate_content(prompt)
                st.success("Here is your Irresistible Pitch! 👇")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {str(e)}. Please check your API key.")
    else:
        st.error("Please fill in all fields!")

st.markdown("---")
st.caption("🔒 Privacy First: Your data and API keys are processed directly in your browser. Nothing is stored. Please review the AI response before sending it to employers.")
