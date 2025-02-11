from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric

fake_data = [
    {
        "input": "I have a persistent cough and fever. Should I be worried?",
        "actual_output": (
            "Based on your symptoms, it could be a sign of a viral or bacterial infection. "
            "However, if the fever persists for more than three days or you experience difficulty breathing, "
            "please consult a doctor immediately."
        ),
        "retrieval_context": [
            "Coughing that lasts more than three weeks is typically classified as a chronic cough and could indicate conditions such as asthma, chronic bronchitis, or gastroesophageal reflux disease (GERD).",
            "A fever is the body's natural response to infections, often caused by viruses or bacteria. Persistent fevers lasting more than three days should be evaluated by a healthcare professional as they may indicate conditions like pneumonia, tuberculosis, or sepsis.",
            "Shortness of breath associated with fever and cough can be a sign of serious respiratory issues such as pneumonia, bronchitis, or COVID-19.",
            "Self-care tips for mild symptoms include staying hydrated, taking over-the-counter fever reducers (e.g., acetaminophen or ibuprofen), and resting. Avoid suppressing a productive cough without consulting a healthcare provider."
        ]
    },
    {
        "input": "What should I do if I accidentally cut my finger deeply?",
        "actual_output": (
            "If you cut your finger deeply, just rinse it with water and avoid applying any pressure. "
            "Tetanus shots aren't necessary unless you see redness immediately."
        ),
        "retrieval_context": [
            "Deep cuts that are more than 0.25 inches deep or expose fat, muscle, or bone require immediate medical attention. Such wounds may need stitches to heal properly.",
            "To minimize the risk of infection, wash the wound thoroughly with soap and water. Avoid using alcohol or hydrogen peroxide, as these can irritate the tissue and delay healing.",
            "If the bleeding persists for more than 10 minutes or soaks through multiple layers of cloth or bandages, seek emergency care. Continuous bleeding might indicate damage to an artery or vein.",
            "Watch for signs of infection, including redness, swelling, warmth, pain, or pus. Infections can develop even in small cuts if not properly cleaned or if the individual is at risk (e.g., diabetic or immunocompromised).",
            "Tetanus, a bacterial infection caused by Clostridium tetani, can enter the body through open wounds. Ensure that your tetanus vaccination is up to date, especially if the wound was caused by a rusty or dirty object."
        ]
    }
]


# Create a list of LLMTestCase
test_cases = []
for fake_datum in fake_data:
  test_case = LLMTestCase(
    input=fake_datum["input"],
    actual_output=fake_datum["actual_output"],
    retrieval_context=fake_datum["retrieval_context"]
  )
  test_cases.append(test_case)

# Define metrics
answer_relevancy = AnswerRelevancyMetric(threshold=0.5)
faithfulness = FaithfulnessMetric(threshold=0.5)

# Run evaluation
evaluate(test_cases=test_cases, metrics=[answer_relevancy, faithfulness])



# OUTPUT : 

# ✨ You're running DeepEval's latest Answer Relevancy Metric! (using gpt-4o, strict=False, async_mode=True)...
# ✨ You're running DeepEval's latest Faithfulness Metric! (using gpt-4o, strict=False, async_mode=True)...
# Evaluating 2 test case(s) in parallel: |████████████████████|100% (2/2) [Time Taken: 00:21, 10.98s/test case]

# ======================================================================

# Metrics Summary

#   - ✅ Answer Relevancy (score: 1.0, threshold: 0.5, strict: False, evaluation model: gpt-4o, reason: The score is 1.00 because the response perfectly and directly addressed the concern about having a persistent cough and fever without including any irrelevant information. Well done!, error: None)
#   - ✅ Faithfulness (score: 1.0, threshold: 0.5, strict: False, evaluation model: gpt-4o, reason: The score is 1.00 because there are no contradictions present, demonstrating perfect alignment between the actual output and the retrieval context. Great job!, error: None)

# For test case:

#   - input: I have a persistent cough and fever. Should I be worried?
#   - actual output: Based on your symptoms, it could be a sign of a viral or bacterial infection. However, if the fever persists for more than three days or you experience difficulty breathing, please consult a doctor immediately.
#   - expected output: None
#   - context: None
#   - retrieval context: ['Coughing that lasts more than three weeks is typically classified as a chronic cough and could indicate conditions such as asthma, chronic bronchitis, or gastroesophageal reflux disease (GERD).', "A fever is the body's natural response to infections, often caused by viruses or bacteria. Persistent fevers lasting more than three days should be evaluated by a healthcare professional as they may indicate conditions like pneumonia, tuberculosis, or sepsis.", 'Shortness of breath associated with fever and cough can be a sign of serious respiratory issues such as pneumonia, bronchitis, or COVID-19.', 'Self-care tips for mild symptoms include staying hydrated, taking over-the-counter fever reducers (e.g., acetaminophen or ibuprofen), and resting. Avoid suppressing a productive cough without consulting a healthcare provider.']

# ======================================================================

# Metrics Summary

#   - ✅ Answer Relevancy (score: 0.5, threshold: 0.5, strict: False, evaluation model: gpt-4o, reason: The score is 0.50 because while the answer provides some relevant information regarding the possible risk of tetanus after a cut, it neglects immediate first-aid steps that are crucial in response to such an injury. Focusing solely on post-injury infection diverts attention from immediate care needed at the moment of injury, leading to an average score., error: None)
#   - ❌ Faithfulness (score: 0.3333333333333333, threshold: 0.5, strict: False, evaluation model: gpt-4o, reason: The score is 0.33 because the actual output advises against applying pressure to stop bleeding, which contradicts the context's suggestion to do so if bleeding persists. Additionally, it overlooks the context's emphasis on updating the tetanus vaccination for wounds from rusty or dirty objects, independent of the presence of redness., error: None)

# For test case:

#   - input: What should I do if I accidentally cut my finger deeply?
#   - actual output: If you cut your finger deeply, just rinse it with water and avoid applying any pressure. Tetanus shots aren't necessary unless you see redness immediately.
#   - expected output: None
#   - context: None
#   - retrieval context: ['Deep cuts that are more than 0.25 inches deep or expose fat, muscle, or bone require immediate medical attention. Such wounds may need stitches to heal properly.', 'To minimize the risk of infection, wash the wound thoroughly with soap and water. Avoid using alcohol or hydrogen peroxide, as these can irritate the tissue and delay healing.', 'If the bleeding persists for more than 10 minutes or soaks through multiple layers of cloth or bandages, seek emergency care. Continuous bleeding might indicate damage to an artery or vein.', 'Watch for signs of infection, including redness, swelling, warmth, pain, or pus. Infections can develop even in small cuts if not properly cleaned or if the individual is at risk (e.g., diabetic or immunocompromised).', 'Tetanus, a bacterial infection caused by Clostridium tetani, can enter the body through open wounds. Ensure that your tetanus vaccination is up to date, especially if the wound was caused by a rusty or dirty object.']

# ======================================================================

# Overall Metric Pass Rates

# Answer Relevancy: 100.00% pass rate
# Faithfulness: 50.00% pass rate

# ======================================================================