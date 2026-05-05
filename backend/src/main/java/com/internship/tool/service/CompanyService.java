package com.internship.tool.service;

import com.internship.tool.entity.Company;
import com.internship.tool.repository.CompanyRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Map;

@Service
public class CompanyService {

    @Autowired
    private CompanyRepository companyRepository;

    @Autowired
    private AiServiceClient aiServiceClient;

    // Create company
    public Company createCompany(Company company) {
        return companyRepository.save(company);
    }

    // Generate report
    public Object generateReport(Company company) {

        Map<String, Object> request = Map.of(
                "company_name", company.getName(),
                "env_score", company.getEnvScore(),
                "social_score", company.getSocialScore(),
                "gov_score", company.getGovScore(),
                "notes", company.getNotes()
        );

        return aiServiceClient.generateReport(request);
    }
}