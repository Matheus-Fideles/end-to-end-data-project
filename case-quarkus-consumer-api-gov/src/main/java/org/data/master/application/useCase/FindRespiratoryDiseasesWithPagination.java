package org.data.master.application.useCase;

import java.util.List;
import java.util.Objects;

import org.data.master.application.domain.model.RespiratoryDiseases;
import org.data.master.application.dto.Pagination;
import org.data.master.application.dto.RespiratoryDiseasesDTO;
import org.data.master.application.port.FindRecords;
import org.jboss.logging.Logger;

import jakarta.enterprise.context.ApplicationScoped;

@ApplicationScoped
public class FindRespiratoryDiseasesWithPagination implements FindRecords {

     private static final Logger logger = Logger.getLogger(FindRespiratoryDiseasesWithPagination.class);

    
    @Override
    public RespiratoryDiseasesDTO execute(Integer year, Integer month, Integer page, Integer size) {
        
        logger.info("Searching for records in the database");
        
        Long totalRecords = RespiratoryDiseases.count();

        Pagination pagination = new Pagination(page, size,  totalRecords / size, totalRecords);

        RespiratoryDiseasesDTO respiratoryDiseasesDTO = new RespiratoryDiseasesDTO(
            getRecords(year, month, page, size),
            pagination
        );

        logger.info("Data successfully collected from the database, filtered and paginated");
        
        
        return respiratoryDiseasesDTO;
    }

    private List<RespiratoryDiseases> getRecords(Integer year, Integer month, Integer page, Integer size) {

        logger.info("Identifying the type of filter and searching for records in the database");

        if(Objects.nonNull(year) && Objects.nonNull(month)) {
            logger.info("executing findRespiratoryDiseasesesByYearAndMonth");
            return RespiratoryDiseases.findRespiratoryDiseasesByYearAndMonth(year, month, page, size);
        } 
        
        if(Objects.nonNull(year)) {
            logger.info("executing findRespiratoryDiseasesesByYear");
            return RespiratoryDiseases.findRespiratoryDiseasesByYear(year, page, size);
        } 
        
        if(Objects.nonNull(month)) {
            logger.info("executing findRespiratoryDiseasesesByMonth");
            return RespiratoryDiseases.findRespiratoryDiseasesByMonth(month, page, size);
        } 
          
        
        logger.info("executing findAllRespiratoryDiseaseses");
        return RespiratoryDiseases.findAllRespiratoryDiseases(page, size);
    }   
    
}
