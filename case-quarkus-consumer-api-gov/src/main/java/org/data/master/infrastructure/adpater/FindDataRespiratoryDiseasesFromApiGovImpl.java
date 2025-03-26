package org.data.master.infrastructure.adpater;

import java.util.List;
import java.util.ArrayList;

import jakarta.inject.Inject;
import org.data.master.application.domain.model.RespiratoryDiseases;
import org.data.master.application.port.FindDataRespiratoryDiseasesFromApiGov;
import org.data.master.infrastructure.api.client.RespiratoryDiseasesGovClient;
import org.eclipse.microprofile.rest.client.inject.RestClient;
import org.jboss.logging.Logger;

import jakarta.enterprise.context.ApplicationScoped;

@ApplicationScoped
public class FindDataRespiratoryDiseasesFromApiGovImpl implements FindDataRespiratoryDiseasesFromApiGov {

    private static final Logger logger = Logger.getLogger(FindDataRespiratoryDiseasesFromApiGovImpl.class);

    @Inject
    @RestClient
    RespiratoryDiseasesGovClient respiratoryDiseasesGovClient;

    @Override
    public List<RespiratoryDiseases> execute(Integer year) {

        List<List<RespiratoryDiseases>> respiratoryDiseasesList = new ArrayList<>();

        for (int month = 1; month <= 12; month++) {
            boolean isEmpty = false;
            int page = 1;

            logger.info("Collection for year: " + year + " and month: " + month);
            while (!isEmpty) {

                int finalMoth = month;
                List<RespiratoryDiseases> respiratoryDiseases = respiratoryDiseasesGovClient
                        .getExtensionsById("" + year + month, page)
                        .stream().map(covid -> {

                            RespiratoryDiseases respiratoryDisease = covid.toDomain();

                            respiratoryDisease.setYears(year);
                            respiratoryDisease.setMonths(finalMoth);
                            return respiratoryDisease;
                        }).toList();

                if (respiratoryDiseases.isEmpty())
                    isEmpty = true;
                else {
                    respiratoryDiseasesList.add(respiratoryDiseases);
                    page++;
                }
            }
        }

        logger.info("Data collected from the government database");
        return respiratoryDiseasesList.stream().flatMap(List::stream).toList();
    }

}