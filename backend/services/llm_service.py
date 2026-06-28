"""
LLM service - Phase 9
Handles communication with language models
"""

from typing import List, Dict
import os
from config import settings


class LLMService:
    """
    Service for interacting with language models
    Currently configured for OpenAI, can be extended for other providers
    """
    
    def __init__(self):
        """Initialize LLM service"""
        self.api_key = settings.openai_api_key
        self.model = settings.openai_model
        # TODO: Import openai when API key is set
    
    def answer_question(self, question: str, context: str) -> str:
        """
        Answer question based on context
        
        Args:
            question: User question
            context: Document context
            
        Returns:
            LLM response
        """
        # TODO: Phase 9 - Implement OpenAI API call
        prompt = f"""Based on the following context, answer the question.

Context:
{context}

Question: {question}

Answer:"""
        
        # This is a placeholder - actual implementation will use OpenAI API
        return "Feature coming in Phase 9"
    
    def summarize(self, text: str, max_length: int = 200) -> str:
        """
        Summarize text
        
        Args:
            text: Text to summarize
            max_length: Max length of summary
            
        Returns:
            Summary
        """
        # TODO: Phase 10 - Implement summarization
        return "Feature coming in Phase 10"
    
    def generate_quiz(self, text: str, num_questions: int = 5) -> List[Dict]:
        """
        Generate quiz questions from text
        
        Args:
            text: Text to generate questions from
            num_questions: Number of questions
            
        Returns:
            List of quiz questions
        """
        # TODO: Phase 10 - Implement quiz generation
        return []
    
    def generate_flashcards(self, text: str) -> List[Dict]:
        """
        Generate flashcards from text
        
        Args:
            text: Text to generate flashcards from
            
        Returns:
            List of flashcards with questions and answers
        """
        # TODO: Phase 10 - Implement flashcard generation
        return []
