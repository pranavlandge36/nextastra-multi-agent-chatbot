from pydantic import BaseModel, Field
from typing import List


class DocumentStyle(BaseModel):
    title_style: str | None = None
    heading_style: str | None = None
    body_style: str | None = None
    font: str | None = None


class DocumentAnalysis(BaseModel):
    document_type: str = Field(
        description="Type of document, such as proposal, report, resume, etc."
    )

    purpose: str = Field(
        description="Main purpose of the document"
    )

    tone: str = Field(
        description="Writing tone of the document"
    )

    sections: List[str] = Field(
        description="Main sections or headings found in the document"
    )

    important_content: List[str] = Field(
        description="Important topics or information contained in the document"
    )

    style: DocumentStyle

class SlideAnalysis(BaseModel):
    slide_number: int
    purpose: str
    layout: str
    key_content: List[str]


class PPTStyle(BaseModel):
    fonts: List[str]
    layouts: List[str]
    visual_style: str


class PPTAnalysis(BaseModel):
    presentation_type: str
    purpose: str
    tone: str
    slide_count: int
    slides: List[SlideAnalysis]
    style: PPTStyle

class SupervisorDecision(BaseModel):
    task_type: str = Field(
        description="Type of task requested by the user"
    )

    agents: List[str] = Field(
        description="Agents that should handle the task"
    )

    reasoning: str = Field(
        description="Short explanation of why these agents are needed"
    )

class ResearchSource(BaseModel):
    title: str
    url: str
    relevance: str


class ResearchResult(BaseModel):
    topic: str
    summary: str
    key_findings: List[str]
    sources: List[ResearchSource]

class EditedSlide(BaseModel):
    title: str
    bullets: List[str]


class EditingResult(BaseModel):
    slides: List[EditedSlide]