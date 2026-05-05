package com.internship.tool.service;

import com.internship.tool.entity.Company;
import com.internship.tool.repository.CompanyRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

import java.util.Map;

@Service
public class CompanyService {

    @Autowired
    private CompanyRepository companyRepository;

    @Autowired
    private AiServiceClient aiServiceClient;

    public Company createCompany(Company company) {
        Company saved = companyRepository.save(company);

        // Call AI in background
        enrichWithAI(saved.getId());

        return saved;
    }

    @Async
    public void enrichWithAI(Long companyId) {
        try {
            Company company = companyRepository.findById(companyId).orElse(null);
            if (company == null) return;

            Map<String, Object> request = Map.of(
                "company_name", company.getName(),
                "env_score", company.getEnvScore(),
                "social_score", company.getSocialScore(),
                "gov_score", company.getGovScore(),
                "notes", company.getNotes()
            );

            String summary = aiServiceClient.getDescription(request);
            Object recommendations = aiServiceClient.getRecommendations(request);

            if (summary != null) {
                company.setAiSummary(summary);
            }

            if (recommendations != null) {
                company.setRecommendations(recommendations.toString());
            }

            companyRepository.save(company);

        } catch (Exception e) {
            System.out.println("AI Error: " + e.getMessage());
        }
    }
}