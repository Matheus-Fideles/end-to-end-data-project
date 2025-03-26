package org.data.master.application.useCase;

import java.util.List;

import org.data.master.application.domain.model.RespiratoryDiseases;
import org.data.master.application.port.CollectingProcessData;
import org.data.master.application.port.FindDataRespiratoryDiseasesFromApiGov;
import org.jboss.logging.Logger;

import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;

@ApplicationScoped
public class CollectingProcessDataUseCase implements CollectingProcessData {

    private static final Logger logger = Logger.getLogger(CollectingProcessDataUseCase.class);


    @Inject
    FindDataRespiratoryDiseasesFromApiGov findDataRespiratoryDiseasesFromApiGov;

    @Override
    public void execute(Integer year) {
        List<RespiratoryDiseases> respiratoryDiseases = findDataRespiratoryDiseasesFromApiGov.execute(year);
        
        logger.info("Saving the records found in the government database to the database");

        respiratoryDiseases.forEach(RespiratoryDiseases::persistAndFlush);

        logger.info("The government database records have been saved to the database");
        
    }
    
}
