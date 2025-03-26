package org.data.master.infrastructure.api;

import jakarta.inject.Inject;
import jakarta.transaction.Transactional;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Response;
import org.data.master.application.port.CollectingProcessData;
import org.data.master.application.port.FindRecords;
import org.jboss.logging.Logger;


@Path("/respiratory-diseases")
public class CaseResource {

    private static final Logger logger = Logger.getLogger(CaseResource.class);

    @Inject
    CollectingProcessData collectingProcessData;

    @Inject
    FindRecords findRecords;

    @POST
    @Path("movement-in-costs/{year}")
    @Transactional
    public Response processGetAllRecordsInYear(Integer year){

        logger.info("receiving requisition for processing government data collection for covid");

        collectingProcessData.execute(year);

        return Response.ok("Processing completed successfully, database loaded for the year mentioned").build();
    }

    @GET
    @Path("movement-in-costs")
    @Transactional
    public Response getAllRecordsInYear(
            @QueryParam("year") Integer year,
            @QueryParam("month") Integer month,
            @QueryParam("page") @DefaultValue("1") Integer page,
            @QueryParam("size") @DefaultValue("10") Integer size
    ){
        logger.info("receiving requisition for getting all records in the database");
        return Response.ok(findRecords.execute(year, month, page, size)).build();
    }
}
