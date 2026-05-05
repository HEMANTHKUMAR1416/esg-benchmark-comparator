package com.internship.tool.entity;

import jakarta.persistence.*;

@Entity
public class Company {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    private int envScore;
    private int socialScore;
    private int govScore;
    private String notes;

    private String aiSummary;
    private String recommendations;

    // Getters & Setters

    public Long getId() { return id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public int getEnvScore() { return envScore; }
    public void setEnvScore(int envScore) { this.envScore = envScore; }

    public int getSocialScore() { return socialScore; }
    public void setSocialScore(int socialScore) { this.socialScore = socialScore; }

    public int getGovScore() { return govScore; }
    public void setGovScore(int govScore) { this.govScore = govScore; }

    public String getNotes() { return notes; }
    public void setNotes(String notes) { this.notes = notes; }

    public String getAiSummary() { return aiSummary; }
    public void setAiSummary(String aiSummary) { this.aiSummary = aiSummary; }

    public String getRecommendations() { return recommendations; }
    public void setRecommendations(String recommendations) { this.recommendations = recommendations; }
}